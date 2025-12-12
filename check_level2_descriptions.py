#!/usr/bin/env python3
"""Проверка записей в level2_descriptions"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import Level2Description
from sqlalchemy import func

def check_level2():
    db = SessionLocal()
    try:
        # Ищем все записи с Dyson
        dyson_records = db.query(Level2Description).filter(
            Level2Description.level_2.like('%Dyson%')
        ).all()
        
        print(f"Найдено {len(dyson_records)} записей с Dyson:")
        for record in dyson_records:
            print(f"  - level_2: '{record.level_2}'")
            print(f"    description: '{record.description[:50] if record.description else 'None'}...'")
            print(f"    details: '{record.details[:50] if record.details else 'None'}...'")
            print()
        
        # Проверяем конкретную запись
        target = "Фен Dyson Nural (HD16)"
        exact = db.query(Level2Description).filter(
            Level2Description.level_2 == target
        ).first()
        
        print(f"\nТочный поиск '{target}':")
        if exact:
            print(f"  ✅ Найдено: {exact.level_2}")
        else:
            print(f"  ❌ Не найдено")
        
        # Поиск без учета регистра
        case_insensitive = db.query(Level2Description).filter(
            func.lower(Level2Description.level_2) == target.lower()
        ).first()
        
        print(f"\nПоиск без учета регистра '{target.lower()}':")
        if case_insensitive:
            print(f"  ✅ Найдено: {case_insensitive.level_2}")
        else:
            print(f"  ❌ Не найдено")
        
        # Показываем все записи
        all_records = db.query(Level2Description).all()
        print(f"\nВсего записей в level2_descriptions: {len(all_records)}")
        
    finally:
        db.close()

if __name__ == "__main__":
    check_level2()
