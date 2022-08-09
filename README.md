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
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/jwt/create/' \
--header 'Content-Type: application/json' \
--data-raw '{
		"username": "your_username",
		"password": "your_password"
}'
```
Формат ответа:
```
{
		"refresh": "string",
		"access": "string"
}
```
2. Получение публикаций:
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4' \
--header 'Content-Type: application/json' \
--data-raw ''
```
Формат ответа:
```
{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=6",
  "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
3. Получение одной публикации по id:
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/1 \
--header 'Content-Type: application/json' \
--data-raw ''
```
Формат ответа:
```
{
		"id": 0,
		"author": "string",
		"text": "string",
		"pub_date": "2019-08-24T14:15:22Z",
		"image": "string",
		"group": 0
}
```
4. Получение комментариев:
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/1/comments' \
--header 'Content-Type: application/json' \
--data-raw ''
```
Формат ответа:
```
[
		{
		"id": 0,
		"author": "string",
		"text": "string",
		"created": "2019-08-24T14:15:22Z",
		"post": 0
		}
]
```
5. Список сообществ:
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/1/groups' \
--header 'Content-Type: application/json' \
--data-raw ''
```
Формат ответа:
```
[
		{
		"id": 0,
		"title": "string",
		"slug": "string",
		"description": "string"
		}
]
```
6. Подписки пользователя, сделавшего запрос (доступно только авторизованным пользователям):
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/follow/' \
--header 'Authorization: Bearer {your_api_yatube_token}' \
--header 'Content-Type: application/json' \
--data-raw ''
```
Формат ответа:
```
[
		{
		"user": "string",
		"following": "string"
		}
]
```
7. Создание подписки на автора(доступно только авторизованным пользователям):
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/follow/' \
--header 'Authorization: Bearer {your_api_yatube_token} \
--header 'Content-Type: application/json' \
--data-raw '{
    "following": "following_username"
}'
```
Формат ответа:
```
{
  "user": "string",
  "following": "string"
}
```
8. Создание публикации (доступно только авторизованным пользователям):
```
curl —location —request POST ‘http://127.0.0.1:8000/api/v1/posts/‘ \
—header ‘Authorization: Bearer {your_api_yatube_token}’ \
—header ‘Content-Type: application/json’ \
—data-raw ‘{
    «text»: «your_text»
}’
```
Формат ответа:
```
{
		"id": 0,
		"author": "string",
		"text": "string",
		"pub_date": "2019-08-24T14:15:22Z",
		"image": "string",
		"group": 0
}
```