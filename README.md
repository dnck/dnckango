# dnckango
Basic webapp in django for learning purposes

## Lesson 1: Passing kwargs to path() for use in view
You can pass kwargs to the path() functions in the urlpatterns list in the urls module for use in view module of an arbitrary dir containing your app. This is interesting because it allows you to use a single view function and modify its return depending on what you provide as input to the path function. For example, if you look at the polls/zoofun page after running python manage.py runserver, you can see that the curse words are censored. If you now flip the switch for censor in the kwargs dict passed to the view function in the urls module, then you can get a naughty page with a funny poem.

## Lesson 2. Choosing a db
For now, I want to make sure in the future my webapp is scalable so I choose to install postgres and psycopg2:
```
apt-get install postgresql-10
pip install psycopg2-binary
```
Note on postgres install for my own UBUNTU computer:
* login to the default postgres username with ```sudo su - postgres```, then enter ```psql```
* each project needs its own database
* create the database for the project with ```CREATE DATABASE projectname;```
* create a user for postgres with ```CREATE USER username WITH PASSWORD 'password';```
You can also set up some things with the database for speed and optimization:
** ```ALTER ROLE projectname SET client_encoding TO 'utf8';```
** ```ALTER ROLE projectname SET default_transaction_isolation TO 'read committed';```
** ```ALTER ROLE projectname SET timezone TO 'UTC';```
I only did the 1st and 3rd
* Give the username all access: ```GRANT ALL PRIVILEGES ON DATABASE projectname TO username;```
* Exit with ```\q``` and then ```exit```
For localhost dev, your ```settings.py``` will now have this block:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projectname ',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
