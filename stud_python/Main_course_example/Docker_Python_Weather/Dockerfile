# Установка базового образа Python
FROM python:3.10

# Копирование кода приложения в образ
COPY . /app

# Установка зависимостей
RUN pip install -r /app/requirements.txt

# Порт, который должен быть открыт при запуске контейнера
EXPOSE 8000

# Запуск скрипта при запуске контейнера
CMD ["python", "/app/app_weather.py"]