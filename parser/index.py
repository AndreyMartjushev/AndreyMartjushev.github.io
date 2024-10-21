import requests
import json
# Сбор данных со страниц с 1 по 58
def fetch_cards(page):
    url = f"https://www.berserkdeck.ru/dev/api/cards?sort=setInfo.ordinal,desc&sort=number&page={page}&size=64"
    response = requests.get(url)
    response.raise_for_status()  # Проверяем наличие ошибок в запросе
    return response.json()

def main():
    all_cards = []

    for page in range(1, 59):  
        data = fetch_cards(page)
        all_cards.extend(data['content'])  # Добавляем содержимое в общий список

    # Сохраняем собранные данные в JSON-файл
    with open('cards.json', 'w', encoding='utf-8') as f:
        json.dump(all_cards, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
