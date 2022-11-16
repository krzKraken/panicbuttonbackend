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
