import json
import re
# Добавляем поле img в каждый элемент

def main():
    # Загружаем данные из JSON-файла
    with open('cards.json', 'r', encoding='utf-8') as f:
        cards = json.load(f)

    # Добавляем поле img в каждый элемент
    for card in cards:
        name = card['name']
        card['img'] = f"/img/{name}.jpg"

    # Сохраняем обновленные данные обратно в JSON-файл
    with open('updated_cards.json', 'w', encoding='utf-8') as f:
        json.dump(cards, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
