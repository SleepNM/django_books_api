# Django Book API

API for storing book informations.

## Instructions

Clone this repisitory and cd into src.

```bash
git clone git@github.com:SleepNoMore/django_books_api.git
cd django_books_api/src
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Run local server

```py
python manage.py runserver
```

## Endpoints

```url
localhost:8000/api/
localhost:8000/api/id/
```
## Task requirements

```text
Django app which allows a user to create list with favorite books and manage it:
- user must be able to see list of books he already added, create new, modify and delete them
- book model must contain following fields:
-- author
-- title
-- description
-- poster image
Back-end requirements:
- Use django-webpack-loader
- Use django-rest-framework
- Use Django's users model
```
