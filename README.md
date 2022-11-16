# SIMPLE CRUD IN DJANGO

## Project Setup

- install a virtual env
  > pip install virtualenv
- create a virtualenv
  > python3 -m virtualenv venv
- activate the virtualenv
  > (windows) .\venv\bin\activate
  > (Linux/mac) ./venv/bin/activate
- install django and restframework
  > pip install django
  > pip install djangorestframework

## Creating the project

- Create the project
  > django-admin startproject panicbuttonproject .
  > (python manage.py runserver -> check if the app is working)

## Creating the app

- Create the app
  > python manage.py startapp panicbuttonapp
- Add the application in the project

\*\*
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
"panicbuttonapp",
"rest_framework"
]
\*\*

## Creating the models

- Create a model in the app panicbuttonapp/models.py
  This models will be the tables in our project

\*\*
class Equipment(models.Model):
brand = models.CharField(max_length=20)
model = models.CharField(max_length=20)
serial_number = models.CharField(max_length=20)
description = models.CharField(max_length=150)
client = models.CharField(max_length=30)
center = models.CharField(max_length=50)
ubication = models.CharField(max_length=50)
reported = models.BooleanField(default=False)
created_at = models.DateTimeField(auto_now_add=True)

\*\*

- Update the db with makemigrations
  > python manage.py makemigrations
- execute the migrations in the db
  > python manage.py migrate

## Creating the rest API

- Create a serializers.py file in the application panicbuttonapp

\*\*

### serializers.py

from rest_framework import serializers
from .models import Equipment

#Convert data in data that we can use and read

class EquipmentSerializer(serializers.ModelSerializer):

class Meta:
model = Equipment
fields = ("id", "brand", "model", "serial_number", "description",
"client", "center", "ubication", "reported", "created_at")
read_only_fields = ("created_at")
\*\*

- Create a api.py file in the applicacion panicbuttonapp

\*\*

### api.py

from .models import Equipment
from rest_framework import viewsets, permissions
from .serializers import EquipmentSerializer

#viewset configures the permissions and the users that can see the data

class EquipmentViewSet(viewsets.ModelViewSet):
queryset = Equipment.objects.all() # permissions_classes = [permissions.IsAuthenticated]
permissions_classes = [permissions.AllowAny]
serializer_class = EquipmentSerializer
\*\*

# Configuring the urls

- Create the urls.py in the application panicbuttonapp

\*\*

### urls.py

from rest_framework import routers
from .api import EquipmentViewSet

router = routers.DefaultRouter()

router.register('api/equipment', EquipmentViewSet, 'equipments')

urlpatterns = router.urls
\*\*

- Configure the urls.py in the panicbuttonproject
  add the urlpatterns created in the panicbuttonapp/urls.py with the include library from django.urls

**
urlpatterns = [
path("admin/", admin.site.urls),
path("", include("panicbuttonapp.urls")), <-- include urls
]
**

# Deploy in render

## configuring the django project

- We need a git account
  > git init
- Ignore all the files in a .gitignore file
  db.sqlite3
  venv
  **pycache**

** render.com/docs/deploy-django **

### GO PRODUCTION - READY

- Go to settings.py in the proyect and import os
  > import os

#### SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

#### SECURITY WARNING: don't run with debug turned on in production!

DEBUG = 'RENDER' not in os.environ

#### https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')if RENDER_EXTERNAL_HOSTNAME: ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Configure the db postgreSQL

- In render go to PostgreSQL
- Create a postgreSQL database in render, put the url and db name and create
- install dj-database-url psycopg2-binary in venv
  > pip install dj-database-url psycopg2-binary
- import the dj-databases-url in the panicbuttonproject
  > import dj-databases-url
- update de database configuration
  DATABASES = {
  'default':
  dj_database_url.config(
  default='sqlite:///db.sqlite3',
  conn_max_age=600,
  )
  }
- Static files configuration
- Install whitenoise[brotli]
  > pip install 'whitenoise[brotli]'
- add middleware in panicbuttonproject/settings.py
  MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  'whitenoise.middleware.WhiteNoiseMiddleware', **<==|**
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
  ]
- modify the panicbuttonproject/settings.py -> STATIC_URL
  STATIC_URL = '/static/'

#Following settings only make sense on production and may break development environments.

if not DEBUG: # Tell Django to copy statics to the `staticfiles` directory # in your application directory on Render.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Turn on WhiteNoise storage backend that takes care of compressing static files # and creating unique names for each version so they can safely be cached forever.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Creating the bash.sh to run a list o commands

- pip freeze > requirements.txt --> Create the list o requirements in the project
- create a build.sh file in the main folder

## build.sh file

#!/usr/bin/env bash
#exit on error

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

- chmod a+x build.sh

- install gunicorn
  > pip install gunicorn
- upload in github

  > git add .
  > git commit -m "ready to deploy"
  > git push -u origin <branch>

- create web services
  - link the github account to the project
  - name the project
  - choose python3
  - modify the build command
    - ./build.sh
  - modify start command
    - gunicorn panicbuttonproject.wsgi <== projectname.wsgi
  - Add the enviroment variables
    DATABASE_URL -> internal DB url in the render postgreSQL  
    SECRET_KEY -> keygenerator in google
    PYTHON -> 3.10.8 version of python using (google: python render.com version)
  - deploy button
  - if are ther any problem change de version of django to 4.0
