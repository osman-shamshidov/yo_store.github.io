#!/usr/bin/env python3
"""SQLAlchemy models for Yo Store app - Refactored Architecture"""

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, Float, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import json

Base = declarative_base()

class Product(Base):
    """
    Товары с уникальным SKU (только конкретные конфигурации)
    Общие карточки получаются через GROUP BY level_2
    """
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(50), unique=True, nullable=False, index=True)  # Уникальный SKU
    name = Column(String(200), nullable=False)
    brand = Column(String(100), nullable=False)
    
    # Иерархия категорий
    level_0 = Column(String(100), nullable=False, index=True)  # Смартфоны, Ноутбуки
    level_1 = Column(String(100))  # 16 Series, MacBook
    level_2 = Column(String(100), index=True)  # iPhone 16, iPhone 16 Pro, Air M2
    
    # Дополнительно
    specifications = Column(Text)  # JSON с характеристиками (color, disk, sim_config и др.)
    stock = Column(Integer, default=0)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    @property
    def color(self):
        """Извлечь цвет из specifications"""
        if self.specifications:
            try:
                specs = json.loads(self.specifications) if isinstance(self.specifications, str) else self.specifications
                return specs.get('color', '')
            except (json.JSONDecodeError, TypeError):
                return ''
        return ''
    
    @property
    def disk(self):
        """Извлечь объем памяти из specifications"""
        if self.specifications:
            try:
                specs = json.loads(self.specifications) if isinstance(self.specifications, str) else self.specifications
                return specs.get('disk', '')
            except (json.JSONDecodeError, TypeError):
                return ''
        return ''
    
    @property
    def sim_config(self):
        """Извлечь конфигурацию SIM из specifications"""
        if self.specifications:
            try:
                specs = json.loads(self.specifications) if isinstance(self.specifications, str) else self.specifications
                return specs.get('sim_config', '')
            except (json.JSONDecodeError, TypeError):
                return ''
        return ''
    
    @property
    def memory(self):
        """Алиас для disk (для обратной совместимости)"""
        return self.disk

class ProductImage(Base):
    """
    Изображения товаров (связь по level_2 + color)
    Один набор изображений для всех вариантов одного цвета одной модели
    """
    __tablename__ = "product_images"
    
    id = Column(Integer, primary_key=True, index=True)
    level_2 = Column(String(100), nullable=False, index=True)  # iPhone 16, iPhone 16 Pro
    color = Column(String(50), nullable=False, index=True)     # Black, Teal, Titanium Desert
    img_list = Column(Text, nullable=False)  # JSON массив изображений
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Уникальный составной индекс
    __table_args__ = (
        UniqueConstraint('level_2', 'color', name='uix_level2_color'),
    )

class Category(Base):
    """
    Иерархия категорий
    Описывает структуру level_0 → level_1 → level_2
    """
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    level_0 = Column(String(100), nullable=False, index=True)
    level_1 = Column(String(100))
    level_2 = Column(String(100))
    description = Column(Text)
    icon = Column(String(500))  # Увеличено для поддержки URL иконок

class SkuVariant(Base):
    """
    Определяет какие поля используются для создания вариантов для каждой категории
    Например: Смартфоны используют ["color", "disk", "sim_config"]
              Ноутбуки используют ["color", "ram", "disk"]
    """
    __tablename__ = "sku_variant"
    
    id = Column(Integer, primary_key=True, index=True)
    level_0 = Column(String(100), unique=True, nullable=False)  # Категория верхнего уровня
    variant_fields = Column(Text, nullable=False)  # JSON массив полей
    created_at = Column(DateTime, default=datetime.utcnow)


class Level2Description(Base):
    """
    Описания и характеристики для level_2 (моделей товаров)
    Один набор описаний для всех вариантов одной модели
    """
    __tablename__ = "level2_descriptions"
    
    id = Column(Integer, primary_key=True, index=True)
    level_2 = Column(String(100), unique=True, nullable=False, index=True)  # iPhone 16, iPhone 16 Pro
    description = Column(Text, nullable=False)  # Основное описание товара
    details = Column(Text, nullable=False)  # JSON с характеристиками (процессор, память, экран и т.д.)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PromoCode(Base):
    """
    Промокоды для скидок
    """
    __tablename__ = "promo_codes"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)  # Код промокода
    discount_type = Column(String(20), nullable=False)  # fixed, percentage, free_item
    discount_value = Column(Float)  # Значение скидки (рубли для fixed, проценты для percentage)
    min_order_amount = Column(Float)  # Минимальная сумма заказа для применения
    free_item_sku = Column(String(50))  # SKU бесплатного товара (для discount_type=free_item)
    free_item_condition = Column(Text)  # JSON условие для бесплатного товара (например, {"category": "Смартфоны"})
    is_active = Column(Boolean, default=True)
    usage_limit = Column(Integer)  # Лимит использований (None = безлимит)
    used_count = Column(Integer, default=0)  # Количество использований
    valid_from = Column(DateTime)
    valid_until = Column(DateTime)
    description = Column(Text)  # Описание промокода
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Order(Base):
    """
    Заказы пользователей
    """
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(50), unique=True, nullable=False, index=True)  # Номер заказа
    customer_name = Column(String(200), nullable=False)
    contact_method = Column(String(50), nullable=False)  # phone, email, telegram, whatsapp
    contact_value = Column(String(200), nullable=False)
    address = Column(Text)
    comment = Column(Text)
    shipping_type = Column(String(50), nullable=False)  # delivery, pickup
    delivery_option = Column(String(100))  # moscow, spb, etc.
    pickup_address = Column(Text)
    delivery_datetime = Column(DateTime)
    total = Column(Float, nullable=False)  # Сумма товаров до скидки
    promo_code = Column(String(50))  # Примененный промокод
    discount_amount = Column(Float, default=0.0)  # Сумма скидки
    final_total = Column(Float, nullable=False)  # Конечная цена заказа (total - discount_amount)
    status = Column(String(50), default="new")  # new, processing, completed, cancelled
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Связь с товарами заказа
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    """
    Товары в заказе
    """
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False, index=True)
    product_name = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    color = Column(String(50))
    memory = Column(String(50))
    sim = Column(String(50))
    ram = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Связи
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
