#!/usr/bin/env python3
"""
Скрипт для добавления всех недостающих level_2 из products в level2_descriptions
Добавляет записи с пустыми description и details для всех level_2, которых еще нет в таблице
"""

import os
import sys

# Добавляем текущую директорию в путь для импортов
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import Product, Level2Description
from sqlalchemy import distinct

def add_missing_level2_descriptions():
    """Добавить все недостающие level_2 из products в level2_descriptions"""
    
    db = SessionLocal()
    
    try:
        # Получаем все уникальные level_2 из products (исключая NULL и пустые строки)
        all_level2_from_products = db.query(distinct(Product.level_2)).filter(
            Product.level_2.isnot(None),
            Product.level_2 != ''
        ).all()
        
        # Преобразуем в список строк
        level2_list = [row[0] for row in all_level2_from_products if row[0]]
        
        print(f"📊 Найдено {len(level2_list)} уникальных level_2 в таблице products")
        
        # Получаем все существующие level_2 из level2_descriptions
        existing_level2 = {row[0] for row in db.query(Level2Description.level_2).all()}
        
        print(f"📋 В таблице level2_descriptions уже есть {len(existing_level2)} записей")
        
        # Находим недостающие
        missing_level2 = [level2 for level2 in level2_list if level2 not in existing_level2]
        
        if not missing_level2:
            print("✅ Все level_2 уже присутствуют в level2_descriptions")
            return
        
        print(f"➕ Найдено {len(missing_level2)} недостающих level_2:")
        for level2 in missing_level2:
            print(f"   - {level2}")
        
        # Добавляем недостающие записи
        added_count = 0
        for level2 in missing_level2:
            try:
                new_desc = Level2Description(
                    level_2=level2,
                    description="",  # Пустое описание
                    details="{}"  # Пустой JSON объект
                )
                db.add(new_desc)
                added_count += 1
            except Exception as e:
                print(f"❌ Ошибка при добавлении {level2}: {e}")
                continue
        
        db.commit()
        print(f"✅ Успешно добавлено {added_count} записей в level2_descriptions")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    add_missing_level2_descriptions()
