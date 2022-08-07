# Проект API_yatube
## Описание проекта
Приложение для работы с проектом Yatube - социальной сетью для публикации личных дневников с возможностью оставлять свои отзывы.

## Установка:
1. Клонировать репозиторий и перейти в него в командной строке:
`git clone git@github.com:mtedoradze/api_final_yatube.git`
2. Cоздать и активировать виртуальное окружение:
`python3 -m venv env`
`source env/bin/activate`
3. Установить зависимости из файла requirements.txt:
`python3 -m pip install --upgrade pip`
`pip install -r requirements.txt`
4. Выполнить миграции:
`python3 manage.py migrate`
5. Запустить проект:
`python3 manage.py runserver`

## Примеры запросов:
1. Получить JWT-токен:
`POST http://127.0.0.1:8000/api/v1/jwt/create/`
2. Обновить JWT-токен:
`POST http://127.0.0.1:8000/api/v1/jwt/refresh/`
3. Проверить JWT-токен:
`POST http://127.0.0.1:8000/api/v1/jwt/verify/`
4. Получение публикаций:
`GET http://127.0.0.1:8000/api/v1/posts/`
5. Получение одной публикации по id:
`GET http://127.0.0.1:8000/api/v1/posts/{id}/`
6. Получение комментариев:
`GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`
7. Список сообществ:
`GET http://127.0.0.1:8000/api/v1/groups/`
10. Подписки пользователя, сделавшего запрос (доступно только авторизованным пользователям):
`GET http://127.0.0.1:8000/api/v1/follow/`
11. Создание публикации (доступно только авторизованным пользователям):
`POST http://127.0.0.1:8000/api/v1/posts/`