Django and Vue Integration 

On Windows 10 Machine

check py --version

Python 3.9.0

pip3 --version

pip 20.3.1

for Virtualenvironment, give commands

pip3 install virtualenvwrapper-win

mkvirtualenv my_django_env

It will create Directory Envs\my_django_env

commands to activate Envrionment

workon my_django_env

pip install django

python -m django --version

3.1.4

django-admin startproject integrate_django_vue

cd integrate_django_vue

python manage.py runserver

vue --version

@vue/cli 4.5.9

vue create frontend_vue

Default Vue 2

cd frontend_vue

npm run serve

make file vue.config.js

change settings.py

python manage.py startapp rentsites

in rentsites

views.py add index funtction

in urls.py add index 

in App.vue add  <router-view />

npm install vue-router

npm install axios

add file router.js

in main.js  add router

in Vue create Services folder

create rentDataService.js

create http-common.js

pip install djangorestframework

pip install markdown      

add setting.py
in INSTALLED_APP add 
    'rest_framework',
    'rentsites',

in models.py add model 

create serializers.py

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

add in admin.py

python manage.py runserver

Change urls.py

browser
http://localhost:8000/api/rentsites/

create RentSitesList.vue

http://localhost:8080/
will show from rest in dev mode

for Production 

npm run build

python manage.py collectstatic

python manage.py runserver

browser
http://localhost:8000/
