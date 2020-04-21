# recipe-api


## Getting started

To start project, run:

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
(env)$ git clone git@github.com:dhruvildave22/recipe-api.git
(env)$ cd recipe-api
(env)$ pip install -r requirements.txt
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```

The API will then be available at http://127.0.0.1:8000

