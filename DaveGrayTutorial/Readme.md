## Create Virtual Enviroment

```python
py -m venv .venv
```
## Activate Virtual Enviroment

```python
.venv/Scripts/activate
```

## Dectivate Virtual Enviroment

```python
dactivate
```

## Install Django

```
py -m pip install Django
```

## Create project

```
django-admin startproject 'project_name'
```

## Run project

```
cd 'project-name'
py manage.py runserver
```

## Add static directory in ``settings.py``

```
import os
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```

## Add media directory in ``settings.py``

```
import os
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```

## Create django apps

```
py manage.py startapp 'app_name'
```


## Add app in ``settings.py``

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name',
]
```

## Migrations

```
py manage.py makemigrations
```

```
py manage.py migrate
```

