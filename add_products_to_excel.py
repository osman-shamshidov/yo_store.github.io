#!/usr/bin/env python3
"""
Скрипт для добавления товаров в current_products-2.xlsx
"""

import pandas as pd
import json
from datetime import datetime

# Читаем существующий файл
df = pd.read_excel('current_products-2.xlsx')

# Новые товары для добавления
new_products = []

# 1. Apple Watch Ultra 3 - все варианты
ultra3_colors_bands = [
    ("Natural Titanium", "Natural", "Milanese Natural Loop"),
    ("Black Titanium", "Black", "Milanese Black Loop"),
    ("Natural Titanium", "Natural", "Trail Loop Natural"),
    ("Black Titanium", "Black", "Trail Loop Black"),
    ("Natural Titanium", "Natural", "Ocean Band Natural"),
    ("Black Titanium", "Black", "Ocean Band Black"),
]

for color_name, color_code, band in ultra3_colors_bands:
    sku = f"awu3{color_code.lower()}{band.lower().replace(' ', '').replace('-', '')}"
    name = f"Apple Watch Ultra 3, 49 мм, {color_name} {band}"
    new_products.append({
        'SKU товара': sku,
        'Название товара*': name,
        'Описание': '',
        'Основная категория (level0)*': 'Умные часы',
        'Подкатегория (level1)*': 'Apple Watch Ultra 3',
        'Детальная категория (level2)*': 'Apple Watch Ultra 3',
        'Бренд': 'Apple',
        'Цена*': 99990,
        'Валюта': 'RUB',
        'Количество на складе': 10,
        'Характеристики (JSON)': json.dumps({"color": color_name, "screen_size": "49mm", "band": band})
    })

# 2. Apple Watch Series 11 - все варианты
s11_variants = [
    ("42 mm", "Space Grey Aluminium", "Space Black/Black", "Black Sport Band", "S/M"),
    ("42 mm", "Space Grey Aluminium", "Space Black/Black", "Black Sport Band", "M/L"),
    ("42 mm", "Silver Aluminium", "Silver/White", "White Sport Band", "S/M"),
    ("42 mm", "Silver Aluminium", "Silver/White", "White Sport Band", "M/L"),
    ("42 mm", "Pink Aluminium", "Pink/White", "Pink Sport Band", "S/M"),
    ("42 mm", "Pink Aluminium", "Pink/White", "Pink Sport Band", "M/L"),
    ("46 mm", "Space Grey Aluminium", "Space Black/Black", "Black Sport Band", "S/M"),
    ("46 mm", "Space Grey Aluminium", "Space Black/Black", "Black Sport Band", "M/L"),
    ("46 mm", "Silver Aluminium", "Silver/White", "White Sport Band", "S/M"),
    ("46 mm", "Silver Aluminium", "Silver/White", "White Sport Band", "M/L"),
    ("46 mm", "Pink Aluminium", "Pink/White", "Pink Sport Band", "S/M"),
    ("46 mm", "Pink Aluminium", "Pink/White", "Pink Sport Band", "M/L"),
]

for size, case, color, band, band_size in s11_variants:
    sku = f"aws11{size.replace(' ', '').replace('mm', '')}{color.split('/')[0].lower().replace(' ', '')}{band_size.lower()}"
    name = f"Apple Watch Series 11, {size}, {case} {band} {band_size}"
    new_products.append({
        'SKU товара': sku,
        'Название товара*': name,
        'Описание': '',
        'Основная категория (level0)*': 'Умные часы',
        'Подкатегория (level1)*': 'Apple Watch S11',
        'Детальная категория (level2)*': 'Apple Watch S11 Sport Band',
        'Бренд': 'Apple',
        'Цена*': 39990 if size == "42 mm" else 42990,
        'Валюта': 'RUB',
        'Количество на складе': 10,
        'Характеристики (JSON)': json.dumps({"color": color, "screen_size": size, "band": band, "band_size": band_size})
    })

# 3. iPad 2024-2025 - все модели
ipad_models = [
    # iPad Air 13 M3
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "128GB", "Space Gray", "Wi-Fi", 89990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "128GB", "Space Gray", "Wi-Fi + Cellular", 98990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "256GB", "Space Gray", "Wi-Fi", 104990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "256GB", "Space Gray", "Wi-Fi + Cellular", 113990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "128GB", "Starlight", "Wi-Fi", 89990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "128GB", "Starlight", "Wi-Fi + Cellular", 98990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "256GB", "Starlight", "Wi-Fi", 104990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "256GB", "Starlight", "Wi-Fi + Cellular", 113990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "128GB", "Blue", "Wi-Fi", 89990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "128GB", "Blue", "Wi-Fi + Cellular", 98990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "256GB", "Blue", "Wi-Fi", 104990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "256GB", "Blue", "Wi-Fi + Cellular", 113990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "128GB", "Purple", "Wi-Fi", 89990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "128GB", "Purple", "Wi-Fi + Cellular", 98990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "256GB", "Purple", "Wi-Fi", 104990),
    ("iPad Air 13 M3", "iPad Air 13", "iPad Air 13 M3", "256GB", "Purple", "Wi-Fi + Cellular", 113990),
    
    # iPad Pro 11 M4
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "256GB", "Space Gray", "Wi-Fi", 119990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "256GB", "Space Gray", "Wi-Fi + Cellular", 129990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "512GB", "Space Gray", "Wi-Fi", 139990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "512GB", "Space Gray", "Wi-Fi + Cellular", 149990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "1TB", "Space Gray", "Wi-Fi", 169990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "1TB", "Space Gray", "Wi-Fi + Cellular", 179990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "256GB", "Silver", "Wi-Fi", 119990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "256GB", "Silver", "Wi-Fi + Cellular", 129990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "512GB", "Silver", "Wi-Fi", 139990),
    ("iPad Pro 11 M4", "iPad Pro 11", "iPad Pro 11 M4", "512GB", "Silver", "Wi-Fi + Cellular", 149990),
    
    # iPad Pro 13 M4
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "256GB", "Space Gray", "Wi-Fi", 149990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "256GB", "Space Gray", "Wi-Fi + Cellular", 159990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "512GB", "Space Gray", "Wi-Fi", 169990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "512GB", "Space Gray", "Wi-Fi + Cellular", 179990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "1TB", "Space Gray", "Wi-Fi", 199990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "1TB", "Space Gray", "Wi-Fi + Cellular", 209990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "256GB", "Silver", "Wi-Fi", 149990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "256GB", "Silver", "Wi-Fi + Cellular", 159990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "512GB", "Silver", "Wi-Fi", 169990),
    ("iPad Pro 13 M4", "iPad Pro 13", "iPad Pro 13 M4", "512GB", "Silver", "Wi-Fi + Cellular", 179990),
    
    # iPad 11th generation
    ("iPad 11", "iPad", "iPad 11th gen", "64GB", "Space Gray", "Wi-Fi", 39990),
    ("iPad 11", "iPad", "iPad 11th gen", "64GB", "Space Gray", "Wi-Fi + Cellular", 49990),
    ("iPad 11", "iPad", "iPad 11th gen", "128GB", "Space Gray", "Wi-Fi", 47990),
    ("iPad 11", "iPad", "iPad 11th gen", "128GB", "Space Gray", "Wi-Fi + Cellular", 57990),
    ("iPad 11", "iPad", "iPad 11th gen", "64GB", "Silver", "Wi-Fi", 39990),
    ("iPad 11", "iPad", "iPad 11th gen", "64GB", "Silver", "Wi-Fi + Cellular", 49990),
    ("iPad 11", "iPad", "iPad 11th gen", "128GB", "Silver", "Wi-Fi", 47990),
    ("iPad 11", "iPad", "iPad 11th gen", "128GB", "Silver", "Wi-Fi + Cellular", 57990),
    ("iPad 11", "iPad", "iPad 11th gen", "64GB", "Pink", "Wi-Fi", 39990),
    ("iPad 11", "iPad", "iPad 11th gen", "64GB", "Pink", "Wi-Fi + Cellular", 49990),
    ("iPad 11", "iPad", "iPad 11th gen", "128GB", "Pink", "Wi-Fi", 47990),
    ("iPad 11", "iPad", "iPad 11th gen", "128GB", "Pink", "Wi-Fi + Cellular", 57990),
]

for model, level1, level2, storage, color, connectivity, price in ipad_models:
    sku = f"ipad{model.lower().replace(' ', '').replace('th', '').replace('gen', '')}{storage.lower().replace('gb', '')}{color.lower().replace(' ', '')}{connectivity.lower().replace(' ', '').replace('+', '').replace('-', '')}"
    # Исправляем название, чтобы избежать дублирования
    if model.startswith("iPad"):
        name = f"{model} {storage} {color} {connectivity}"
    else:
        name = f"iPad {model} {storage} {color} {connectivity}"
    specs = {
        "disk": storage,
        "color": color,
        "screen_size": "11\"" if "11" in model else ("13\"" if "13" in model else "10.9\""),
        "sim_config": connectivity
    }
    new_products.append({
        'SKU товара': sku,
        'Название товара*': name,
        'Описание': '',
        'Основная категория (level0)*': 'Планшеты',
        'Подкатегория (level1)*': level1,
        'Детальная категория (level2)*': level2,
        'Бренд': 'Apple',
        'Цена*': price,
        'Валюта': 'RUB',
        'Количество на складе': 10,
        'Характеристики (JSON)': json.dumps(specs)
    })

# 4. Whoop - все модели
whoop_models = [
    ("Whoop 5.0", "Whoop 5.0", "Whoop 5.0", "Black", 0, "Подписка продается отдельно"),
    ("Whoop MG", "Whoop MG", "Whoop MG", "Black", 0, "Подписка продается отдельно"),
    ("Whoop Life 5.0", "Whoop Life", "Whoop Life 5.0", "Black", 31500, "С подпиской 1 год"),
    ("Whoop Life MG", "Whoop Life", "Whoop Life MG", "Black", 33500, "С подпиской 1 год"),
]

for model, level1, level2, color, price, desc in whoop_models:
    sku = f"whoop{model.lower().replace(' ', '').replace('.', '')}{color.lower()}"
    name = f"{model} {color}"
    if desc:
        name += f" - {desc}"
    # Убираем дублирование "Whoop Whoop"
    if name.startswith("Whoop Whoop"):
        name = name.replace("Whoop Whoop", "Whoop", 1)
    new_products.append({
        'SKU товара': sku,
        'Название товара*': name,
        'Описание': desc if desc else '',
        'Основная категория (level0)*': 'Умные браслеты',
        'Подкатегория (level1)*': level1,
        'Детальная категория (level2)*': level2,
        'Бренд': 'Whoop',
        'Цена*': price if price > 0 else 0,
        'Валюта': 'RUB',
        'Количество на складе': 10,
        'Характеристики (JSON)': json.dumps({"color": color})
    })

# 5. Steam Deck - все модели
steam_deck_models = [
    ("Steam Deck LCD", "Steam Deck", "Steam Deck LCD", "64GB", 39990),
    ("Steam Deck LCD", "Steam Deck", "Steam Deck LCD", "256GB", 49990),
    ("Steam Deck LCD", "Steam Deck", "Steam Deck LCD", "512GB", 59990),
    ("Steam Deck OLED", "Steam Deck", "Steam Deck OLED", "512GB", 69990),
    ("Steam Deck OLED", "Steam Deck", "Steam Deck OLED", "1TB", 89990),
]

for model, level1, level2, storage, price in steam_deck_models:
    sku = f"steamdeck{model.lower().replace(' ', '')}{storage.lower().replace('gb', '')}"
    name = f"{model} {storage}"
    new_products.append({
        'SKU товара': sku,
        'Название товара*': name,
        'Описание': '',
        'Основная категория (level0)*': 'Игровые приставки',
        'Подкатегория (level1)*': level1,
        'Детальная категория (level2)*': level2,
        'Бренд': 'Valve',
        'Цена*': price,
        'Валюта': 'RUB',
        'Количество на складе': 10,
        'Характеристики (JSON)': json.dumps({"disk": storage, "color": "Black"})
    })

# Проверяем, какие товары уже есть (по SKU)
existing_skus = set(df['SKU товара'].astype(str).str.lower())

# Фильтруем новые товары, исключая дубликаты
unique_new_products = []
for product in new_products:
    sku_lower = str(product['SKU товара']).lower()
    if sku_lower not in existing_skus:
        unique_new_products.append(product)
        existing_skus.add(sku_lower)

print(f"Найдено новых товаров для добавления: {len(unique_new_products)}")
print(f"Всего товаров в файле до добавления: {len(df)}")

# Создаем DataFrame из новых товаров
new_df = pd.DataFrame(unique_new_products)

# Объединяем с существующими данными
df_updated = pd.concat([df, new_df], ignore_index=True)

# Сохраняем в файл
output_file = 'current_products-2.xlsx'
df_updated.to_excel(output_file, index=False)
print(f"✅ Добавлено {len(unique_new_products)} новых товаров")
print(f"✅ Всего товаров в файле: {len(df_updated)}")
print(f"✅ Файл сохранен: {output_file}")

