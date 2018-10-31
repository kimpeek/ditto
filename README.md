# ditto

URL shortening service built with Django and hosted on Heroku.

[View the app live](http://www.ditto.pink/)

![Create](https://i.imgur.com/3DLTF0d.png)

![copy](https://i.imgur.com/dOSF9ae.png)

## Develop

1. Fork it
1. Clone it to your machine
1. Create a virtualenv
    ```bash
    $ virtualenv venv
    ```
1. Install dependencies
    ```bash
    $ pip install -r requirements
    ```
1. Migrate
    ```bash
    $ py manage.py migrate
    ```
1. Run the dev server
    ```bash
    $ py manage.py runserver
    ```

## Deploy

```bash
$ git init
$ git add .
$ git commit -m "Initial commit"

$ heroku create
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set SECRET_KEY=***YOUR_SECRET_KEY_HERE***
$ heroku config:set ADMIN_URL=administration/

$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
```

---

Design by [PatrickWalters.Design](http://www.patrickwalters.design/)
