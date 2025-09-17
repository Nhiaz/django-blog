# Django Blog

Учебный проект блога на **Django 5**.  
Реализован в рамках изучения веб-разработки с использованием Django.

![Главная страница блога](https://i.imgur.com/gRSZN9K.png)

## ✨ Возможности
- Регистрация и аутентификация пользователей
- Создание, редактирование и удаление постов
- Панель администратора Django
- Использование шаблонов и маршрутов (URL)

## 🛠️ Стек технологий
- Python 3.12+
- Django 5.x
- HTML/CSS (оформление)
- SQLite (база данных по умолчанию)
- [uv](https://github.com/astral-sh/uv) для управления зависимостями и запуском

## 📂 Структура проекта
```angular2html
django-blog/
│── blog_app/          # приложение блога
│   ├── static/        # статика (css, js, изображения)
│   ├── templates/     # HTML-шаблоны приложения
│── blog/       # настройки проекта
│── manage.py
│── pyproject.toml     # зависимости для uv
│── README.md

```

## 🚀 Установка и запуск
Клонируйте репозиторий:

```bash
git clone https://github.com/Nhiaz/django-blog.git
cd django-blog
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

После этого проект будет доступен по адресу:
👉 http://127.0.0.1:8000/blog
