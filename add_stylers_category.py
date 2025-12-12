#!/usr/bin/env python3
"""
Скрипт для добавления/обновления категории "Фены и стайлеры" с иконкой
"""

import os
import sys

# Добавляем текущую директорию в путь для импортов
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import Category

def add_stylers_category():
    """Добавить или обновить категорию Фены и стайлеры с иконкой"""
    
    db = SessionLocal()
    
    try:
        # Иконка для категории Фены и стайлеры
        stylers_icon = "https://appletrade.ru/img/43748831_1920_q70.webp"
        
        # Проверяем, существует ли категория "Стайлеры" (старое название)
        old_category_stylers = db.query(Category).filter(
            Category.level_0 == "Стайлеры",
            Category.level_1 == None,
            Category.level_2 == None
        ).first()
        
        # Проверяем, существует ли категория "Фены/стайлеры" (старое название)
        old_category_slash = db.query(Category).filter(
            Category.level_0 == "Фены/стайлеры",
            Category.level_1 == None,
            Category.level_2 == None
        ).first()
        
        # Проверяем, существует ли категория "Фены и стайлеры" (новое название)
        existing_category = db.query(Category).filter(
            Category.level_0 == "Фены и стайлеры",
            Category.level_1 == None,
            Category.level_2 == None
        ).first()
        
        # Переименовываем старые категории, если они существуют
        if old_category_slash and not existing_category:
            old_category_slash.level_0 = "Фены и стайлеры"
            old_category_slash.icon = stylers_icon
            old_category_slash.description = old_category_slash.description or "Фены и стайлеры для волос"
            print(f"✅ Категория 'Фены/стайлеры' переименована в 'Фены и стайлеры'")
        elif old_category_stylers and not existing_category:
            old_category_stylers.level_0 = "Фены и стайлеры"
            old_category_stylers.icon = stylers_icon
            old_category_stylers.description = old_category_stylers.description or "Фены и стайлеры для волос"
            print(f"✅ Категория 'Стайлеры' переименована в 'Фены и стайлеры'")
        elif existing_category:
            # Обновляем существующую категорию
            existing_category.icon = stylers_icon
            existing_category.description = existing_category.description or "Фены и стайлеры для волос"
            print(f"✅ Категория 'Фены и стайлеры' обновлена с иконкой")
        else:
            # Создаем новую категорию
            new_category = Category(
                level_0="Фены и стайлеры",
                level_1=None,
                level_2=None,
                description="Фены и стайлеры для волос",
                icon=stylers_icon
            )
            db.add(new_category)
            print(f"✅ Категория 'Фены и стайлеры' добавлена с иконкой")
        
        db.commit()
        print("✅ Изменения сохранены в базу данных")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_stylers_category()
