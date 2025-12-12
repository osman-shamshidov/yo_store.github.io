#!/usr/bin/env python3
"""
Скрипт для добавления/обновления категории "Планшеты" с иконкой
"""

import os
import sys

# Добавляем текущую директорию в путь для импортов
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import Category

def add_tablets_category():
    """Добавить или обновить категорию Планшеты с иконкой"""
    
    db = SessionLocal()
    
    try:
        # Иконка для категории Планшеты
        tablets_icon = "https://static.re-store.ru/upload/resize_cache/iblock/bb5/100500_800_140cd750bba9870f18aada2478b24840a/bmyghidv162rz0n4laktfid53b2w0qtf.jpg"
        
        # Проверяем, существует ли категория Планшеты (level_0 только, без level_1 и level_2)
        existing_category = db.query(Category).filter(
            Category.level_0 == "Планшеты",
            Category.level_1 == None,
            Category.level_2 == None
        ).first()
        
        if existing_category:
            # Обновляем существующую категорию
            existing_category.icon = tablets_icon
            existing_category.description = existing_category.description or "Планшетные компьютеры"
            print(f"✅ Категория 'Планшеты' обновлена с иконкой")
        else:
            # Создаем новую категорию
            new_category = Category(
                level_0="Планшеты",
                level_1=None,
                level_2=None,
                description="Планшетные компьютеры",
                icon=tablets_icon
            )
            db.add(new_category)
            print(f"✅ Категория 'Планшеты' добавлена с иконкой")
        
        db.commit()
        print("✅ Изменения сохранены в базу данных")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_tablets_category()



