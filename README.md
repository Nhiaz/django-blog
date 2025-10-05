# Django Blog

Учебный проект блога на **Django 5**.
Реализован в рамках изучения веб-разработки с использованием Django.

![Главная страница блога](https://i.imgur.com/gRSZN9K.png)

## ✨ Возможности
- Регистрация и аутентификация пользователей
- Создание, редактирование и удаление постов
- Добавление и отображение комментариев
- Отправка поста по email (share)
- Панель администратора Django
- Пагинация списка постов
- SEO‑дружественные slug-и

## 🛠️ Стек технологий
- Python 3.12+
- Django 5.x
- SQLite (по умолчанию для разработки)
- HTML / Django Templates / CSS
- [uv](https://github.com/astral-sh/uv) для управления зависимостями

## 📂 Структура проекта
```
django-blog/
├── blog/                # Конфигурация проекта (settings, urls, wsgi, asgi)
├── blog_app/            # Приложение блога (models, views, forms, admin, urls)
│   ├── migrations/      # Миграции БД
│   └── static/
│       └── css/
│           └── blog.css
├── templates/           # Глобальные шаблоны и шаблоны приложения
│   ├── pagination.html
│   └── blog_app/
│       ├── base.html
│       └── post/
│           ├── list.html
│           ├── detail.html
│           ├── share.html
│           ├── comment.html
│           └── includes/
│               └── comment_form.html
├── db.sqlite3           # База данных (development)
├── main.py              # Доп. скрипт (если используется)
├── manage.py            # Утилита управления Django
├── pyproject.toml       # Зависимости и конфигурация (uv)
├── uv.lock              # Зафиксированные версии пакетов
└── README.md            # Документация
```

## 🚀 Установка и запуск
Клонируйте репозиторий и установите зависимости:

```bash
git clone https://github.com/Nhiaz/django-blog.git
cd django-blog
uv sync
```

Примените миграции и запустите сервер разработки:

```bash
uv run manage.py migrate
uv run manage.py runserver
```

Создайте суперпользователя (для доступа в админку):

```bash
uv run manage.py createsuperuser
```

Откройте в браузере: http://127.0.0.1:8000/blog

## 🧪 Тесты
(Опционально) Запуск встроенных тестов приложения:
```bash
uv run python manage.py test
```

## 📌 Дальнейшие улучшения (идеи)
- Поиск по постам
- Теги / рубрики
- Счётчик просмотров или популярные посты (кеш)
- RSS/Atom лента
- Docker-файл для деплоя

## 📄 Лицензия
Свободно для учебных целей.

---
Если хочешь сделать упор на другую часть (например, документацию API или деплой) — напиши, обновлю разделы.
