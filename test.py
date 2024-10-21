import pytesseract
from PIL import Image
import os

# Укажите путь к исполняемому файлу Tesseract, если это необходимо
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def recognize_text(image_path):
    # Открываем изображение
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Ошибка при открытии изображения: {e}")
        return

    # Распознаем текст
    text = pytesseract.image_to_string(image, lang='rus')
    return text

if __name__ == "__main__":
    # Укажите путь к изображению
    image_path = './test3.jpg'
    
    # Получаем распознанный текст
    recognized_text = recognize_text(image_path)
    print("Распознанный текст:")
    print(recognized_text)
