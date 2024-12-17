# Тестовое задание

Этот проект представляет собой  API для управления библиотекой, построенный с использованием FastAPI.

## Настройка

1. Клонируйте репозиторий.

2. Заполните поля в файле .env.sample
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=

3. Переименуйте файл .env.sample в .env

4. Введите команду в командную строку:
docker-compose up -d --build

5. Откройте ваш браузер и перейдите по адресу `http://127.0.0.1:8000/docs`, чтобы увидеть документацию Swagger.

## Тесты

Тесты в проекте написаны для всех эндпоинтов, но они используют отновную бд проекта.
Для запуска тестов:

1. Переименуйте файл .env.sample в .env
2. Заполните пустые места в файле .env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=localhost
POSTGRES_PORT=

3. Запустите тесты командой 
pytest
