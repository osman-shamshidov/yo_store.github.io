#!/usr/bin/env python3
"""
Скрипт для добавления/обновления категории "Наушники" с иконкой
"""

import os
import sys

# Добавляем текущую директорию в путь для импортов
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import Category

def add_headphones_category():
    """Добавить или обновить категорию Наушники с иконкой"""
    
    db = SessionLocal()
    
    try:
        # Иконка для категории Наушники
        headphones_icon = "https://appletrade.ru/img/47684839_1920_q70.webp"
        
        # Проверяем, существует ли категория Наушники (level_0 только, без level_1 и level_2)
        existing_category = db.query(Category).filter(
            Category.level_0 == "Наушники",
            Category.level_1 == None,
            Category.level_2 == None
        ).first()
        
        if existing_category:
            # Обновляем существующую категорию
            existing_category.icon = headphones_icon
            existing_category.description = existing_category.description or "Наушники и аудиоаксессуары"
            print(f"✅ Категория 'Наушники' обновлена с иконкой")
        else:
            # Создаем новую категорию
            new_category = Category(
                level_0="Наушники",
                level_1=None,
                level_2=None,
                description="Наушники и аудиоаксессуары",
                icon=headphones_icon
            )
            db.add(new_category)
            print(f"✅ Категория 'Наушники' добавлена с иконкой")
        
        db.commit()
        print("✅ Изменения сохранены в базу данных")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_headphones_category()
