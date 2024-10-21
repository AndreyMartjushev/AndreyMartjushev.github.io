import requests
import json
import os
 # Сохраняем изображение
# Создаем папку для сохранения изображений, если ее нет
os.makedirs('img', exist_ok=True)

def fetch_image(set_ordinal, number, name):
    url = f"https://www.berserkdeck.ru/dev/api/images/cards-heroes/{set_ordinal}/{number}/regular"
    response = requests.get(url)
    if response.status_code == 200:
        # Сохраняем изображение
        image_path = os.path.join('img', f"{name}.jpg")
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Сохранено изображение: {image_path}")
    else:
        print(f"Не удалось загрузить изображение для {name}. Статус: {response.status_code}")

def main():
    # Загружаем данные из JSON-файла
    with open('cards.json', 'r', encoding='utf-8') as f:
        cards = json.load(f)

    # Проходим по карточкам и загружаем изображения
    for card in cards:
        set_ordinal = card['setInfo']['ordinal']
        number = card['number']
        name = card['name'].replace('/', '_')  # Заменяем символы, которые могут быть в имени
        fetch_image(set_ordinal, number, name)

if __name__ == "__main__":
    main()
