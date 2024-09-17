# Задание 1 Task Manager API

Этот проект представляет собой простой RESTful API для управления списком задач. API разработан с использованием **Django** и **Django REST Framework**. Позволяет выполнять CRUD операции (создание, получение, обновление и удаление задач).

## Установка и запуск проекта

### 1. Клонирование репозитория
Сначала клонируйте репозиторий с проектом:

```bash
git clone git@github.com:Gordey3000/TestGIT.git
cd TestGIT
```

### 2. Создание виртуального окружения
```bash
python -m venv env
source env/bin/activate  # Для Linux/macOS
env\Scripts\activate      # Для Windows
```

### 3. Установка зависимостей

Установите необходимые зависимости, выполнив команду:
```bash
pip install -r requirements.txt
```

### 4. Применение миграций и запуск сервера

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Сервер будет доступен по адресу: http://127.0.0.1:8000/.

## Использование API

### Список задач (GET)

Получение списка всех задач:
```bash
GET /tasks/
```

### Создание новой задачи (POST)

```bash
POST /tasks/
```
тело запроса

```bash
{
  "title": "Название задачи",
  "description": "Описание задачи",
  "completed": false
}

```

### Получение одной задачи (GET)

```bash
GET /tasks/{id}/
```

### Полное обновление задачи (PUT)

```bash
PUT /tasks/{id}/
```
тело запроса:

```bash
{
  "title": "Обновленное название задачи",
  "description": "Обновленное описание задачи",
  "completed": true
}

```

### Частичное обновление задачи (PATCH)

```bash
PATCH /tasks/{id}/
```

тело запроса:

```bash
{
  "completed": true
}
```

### Удаление задачи (DELETE)

```bash
DELETE /tasks/{id}/
```

### Тестирование

Для запуска тестов выполните команду:

```bash
python manage.py test
```