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

get api on url https://my-recipe-api-is-best.herokuapp.com/api/user/create/

## endpoints

create user: https://my-recipe-api-is-best.herokuapp.com/api/user/create/

get token for login: https://my-recipe-api-is-best.herokuapp.com/api/user/token/

for recipe models : https://my-recipe-api-is-best.herokuapp.com/api/recipe/

tags: https://my-recipe-api-is-best.herokuapp.com/api/recipe/tags/

ingredients: https://my-recipe-api-is-best.herokuapp.com/api/recipe/ingredients/

recipes: https://my-recipe-api-is-best.herokuapp.com/api/recipe/recipes/
