# Task API

Task API — это RESTful-сервис на Django + Django REST Framework, предназначенный для управления задачами через API. Сервис позволяет создавать, просматривать, обновлять и удалять задачи. Данные хранятся в PostgreSQL. Проект разворачивается с помощью Docker.

## Возможности

- CRUD-операции с задачами
- Поля задачи: title, description, status
- Автоматическая документация через Swagger и ReDoc
- Поддержка PostgreSQL
- Быстрый запуск через Docker Compose

## Зависимости

Основные зависимости (см. requirements.txt):

```
Django>=4.2
djangorestframework
psycopg2-binary
python-decouple
drf-yasg
```

## Установка и запуск

### 1. Клонирование репозитория

```
git clone https://github.com/christina-mariaa/burkova_api_exam
cd task-api
```

### 2. Создание .env файла

В корне проекта создайте файл `.env` со следующим содержимым:

```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

### 3. Сборка и запуск контейнеров

```
docker compose up --build
```

После запуска проект будет доступен по адресу: `http://localhost:8000`

## Документация API

- Swagger UI: http://localhost:8000/swagger/

## Примеры запросов

### POST /tasks/

```
{
  "title": "Написать отчёт",
  "description": "Финальный отчёт по проекту",
  "status": "todo"
}
```

### PUT /tasks/1/

```
{
  "title": "Обновить отчёт",
  "description": "Финальная версия + исправления",
  "status": "in_progress"
}
```

## Полезные команды

```
# Применить миграции
docker compose exec web python manage.py migrate

```

## Лицензия

Проект создан для учебных целей. Разрешено использование и модификация.
