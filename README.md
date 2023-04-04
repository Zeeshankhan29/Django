# Django - Working with Django framework


creating a virtual env and activate 
```
conda create --name django python==3.10 -y
conda activate django

```

installing django framework

```
pip install django
pip install djangorestframework

```

create django project

```
django-admin startproject <project_name>

```

To evaluate django server

```
cd <change the directory>
django manage.py runserver
default django runs on 8000 port number

```

To run all the default tables 

```
python manage.py makemigrations
python manage.py migrate

```

To find all the commands
```
python manage.py

```

create superuser to access admin

```
python manage.py createsuperuser

```

Django follows a pattern like
```
manage.py --> settings.py --> urls.py --> other weburls

```

Create a new app
```
python manage.py startapp <app name>

```


