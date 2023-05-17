import requests
from bs4 import BeautifulSoup
import csv


def get_unique_words(url):
    # Отправляем GET-запрос на указанный URL и получаем содержимое страницы
    response = requests.get(url)
    html_content = response.text

    # Создаем объект BeautifulSoup для парсинга HTML-контента
    soup = BeautifulSoup(html_content, 'html.parser')

    # Извлекаем текст со страницы
    text = soup.get_text()

    # Разделяем текст на отдельные слова
    words = text.split()

    # Удаляем символы пунктуации и приводим слова к нижнему регистру
    words = [word.lower().strip(".,?!") for word in words]

    # Получаем уникальные слова
    unique_words = set(words)

    return unique_words

# Пример использования


url = 'https://www.radiouniversum.cz/pelz-petr-3d-bezesporu-\
    konci-westernizace-\
    celeho-sveta-a-z-toho-mame-strach-opravnene/'
# Замените ссылку на нужную вам страницу
unique_words = get_unique_words(url)

# Сохраняем список уникальных слов в файл CSV
with open('unique_words.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Unique Words'])
    writer.writerows([[word] for word in unique_words])

print("Список уникальных слов сохранен в файл unique_words.csv")
