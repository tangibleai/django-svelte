# django-svelte
A template for Django/Svelte single-page apps

This gives you [JSON Web Token](https://jwt.io/) auth and a few extra files to help you deploy with heroku. I've left a few `TODO`s in the code, so you can set up your own app. You can see what the template looks like [here](https://django-svelte.herokuapp.com), but I'm not sure why you would want to, because it only lets you log in

## Tech stack

### Web
- [Svelte 3](https://svelte.dev/)
- [webpack](https://webpack.js.org/)

### Mobile
- [React Native](https://facebook.github.io/react-native/)
- [expo](https://github.com/expo/expo)

### Backend
- [Python 3.7](https://www.python.org/)
- [Django](https://www.djangoproject.com/) with ([Django REST framework](https://www.django-rest-framework.org/))
- [gunicorn](https://gunicorn.org/)
- [Whitenoise](http://whitenoise.evans.io/en/stable/)

## Instructions

### Set environment variables
- `DATABASE_URL`. For example, my local value is `postgres://christiandrappi@localhost:5432/django_svelte`
- `PYTHONPATH`. Point it to the outer `backend` dir, since our python does not live in the root directory
- `DJANGO_SECRET_KEY`. Create one with:  
    ```
    $ python
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    ```

### Running locally

Backend Django server (port 8000):  
`$ python backend/manage.py runserver --settings=backend.settings.dev`

Frontend Svelte server (port 8080):  
`$ cd frontend`  
`$ npm run dev`  


### Deploying to Heroku
- Use the buildpack [negativetwelve/heroku-buildpack-subdir](https://github.com/negativetwelve/heroku-buildpack-subdir):  
```$ heroku buildpacks:set https://github.com/negativetwelve/heroku-buildpack-subdir```
- This uses the `.buildpacks` definition in the app root


## Running local dev server

```
$ conda activate django-svelte
$ pip install -r requirements.txt
$ source setup.sh
$ python backend/manage.py runserver --settings=backend.settings.dev`
```

```
(base) hobs@tangibleai-laptop:~/code/tangibleai/django-svelte$ cd frontend
(base) hobs@tangibleai-laptop:~/code/tangibleai/django-svelte/frontend$ npm install

up to date, audited 1 package in 163ms

found 0 vulnerabilities
(base) hobs@tangibleai-laptop:~/code/tangibleai/django-svelte/frontend$ npm run dev
npm ERR! missing script: dev

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/hobs/.npm/_logs/2021-04-24T04_46_16_381Z-debug.log
(base) hobs@tangibleai-laptop:~/code/tangibleai/django-svelte/frontend$ npm run
(base) hobs@tangibleai-laptop:~/code/tangibleai/django-svelte/frontend$ 
```
