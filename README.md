On Windows 10 Machine

C:\Users>py --version
Python 3.9.0

C:\Users>pip3 list
Package    Version
---------- -------
pip        20.2.3
setuptools 49.2.1

command prompt


C:\Users>pip3 install virtualenvwrapper-win

C:\Users>mkvirtualenv my_django_env

It will create Directory Envs\my_django_env


commands to activate Envrionment


C:\Users>workon my_django_env
(my_django_env) C:\Users>pip install django

check
(my_django_env) C:\Users>python -m django --version
3.1.4

(my_django_env) C:\Users>django-admin startproject integrate_django_vue
(my_django_env) C:\Users>cd integrate_django_vue
(my_django_env) C:\Users\integrate_django_vue>python manage.py runserver
check in browser url 
http://localhost:8000/
to see The install worked successfully! Congratulations!

Stop with ctrl+c

(my_django_env) C:\Users\integrate_django_vue>vue --version
@vue/cli 4.5.9

(my_django_env) C:\Users\integrate_django_vue>vue create frontend_vue
Default Vue 2

(my_django_env) C:\Users\integrate_django_vue>cd frontend_vue
npm run serve

check in browser url
http://localhost:8080/
Welcome to Your Vue.js App
(my_django_env) C:\Users\integrate_django_vue\frontend_vue>

make file vue.config.js

change settings.py

#-----------------------------
(my_django_env) C:\Users\integrate_django_vue>python manage.py startapp rentsites

in rentsites
# views.py add index funtction

#--------------------
in urls.py add index 

---------------
in App.vue only  <router-view />

npm install vue-router

npm install axios

add router.js

in main.js  add router
//------------------
in Vue create Services folder
create rentDataService.js

//-----------------
and create http-common.js

//-------------------------
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.


add settinng.py
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

C:\Users\integrate_django_vue\frontend_vue> npm run build
go to (my_django_env) C:\Users\integrate_django_vue>
python manage.py collectstatic
python manage.py runserver
browser
http://localhost:8000/
