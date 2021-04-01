# django

enable run script ps1

- Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

- Set-ExecutionPolicy RemoteSigned -Scope CurrentUser 1 .\Scripts\activate.ps1
- pip install django
- django-admin.exe startproject mysite
- cd .\mysite\
- python.exe .\manage.py migrate
- python.exe .\manage.py startapp blog
- edit settings.py then add your apps in it
- python.exe .\manage.py makemigrations blog
- python manage.py sqlmigrate blog 0001
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver