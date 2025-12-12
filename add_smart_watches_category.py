#!/usr/bin/env python3
"""
Скрипт для добавления/обновления категории "Умные часы" с иконкой
"""

import os
import sys

# Добавляем текущую директорию в путь для импортов
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import Category

def add_smart_watches_category():
    """Добавить или обновить категорию Умные часы с иконкой"""
    
    db = SessionLocal()
    
    try:
        # Иконка для категории Умные часы
        smart_watches_icon = "https://appletrade.ru/img/48064627_1920_q70.webp"
        
        # Проверяем, существует ли категория Умные часы (level_0 только, без level_1 и level_2)
        existing_category = db.query(Category).filter(
            Category.level_0 == "Умные часы",
            Category.level_1 == None,
            Category.level_2 == None
        ).first()
        
        if existing_category:
            # Обновляем существующую категорию
            existing_category.icon = smart_watches_icon
            existing_category.description = existing_category.description or "Умные часы и смарт-часы"
            print(f"✅ Категория 'Умные часы' обновлена с иконкой")
        else:
            # Создаем новую категорию
            new_category = Category(
                level_0="Умные часы",
                level_1=None,
                level_2=None,
                description="Умные часы и смарт-часы",
                icon=smart_watches_icon
            )
            db.add(new_category)
            print(f"✅ Категория 'Умные часы' добавлена с иконкой")
        
        db.commit()
        print("✅ Изменения сохранены в базу данных")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_smart_watches_category()



