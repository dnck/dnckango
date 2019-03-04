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
### Install and CONFIG for UBUNTU & MacOS:
* login to the default postgres username with ```sudo su - postgres```, then enter ```psql```

* On MacOSX, you need to export the the bin directory of the psql command when you log in to postgres user. You can find this in the installation notes. I have to do this every time I login to the postgres user with ```export PATH=/Library/PostgreSQL/11/bin:$PATH```

* Each project needs its own database

* Create the database for the project with ```CREATE DATABASE projectname;```

* Create a user for postgres with ```CREATE USER user WITH PASSWORD 'password';```

  * Yes, you need the quotes around the password you enter.

You can also set up some things with the database for speed and optimization. For example,

* ```ALTER ROLE user SET client_encoding TO 'utf8';```

* ```ALTER ROLE user SET default_transaction_isolation TO 'read committed';```

* ```ALTER ROLE user SET timezone TO 'UTC';```

*I only did the 1st and 3rd options*

* Give the name all access on the db: ```GRANT ALL PRIVILEGES ON DATABASE projectname TO user;```

* Exit with ```\q``` and then ```exit```

For localhost development, your ```settings.py``` will now have this block:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projectname ',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
After installing all this, you should execute, ```python manage.py migrate```

* If you did part of the tutorial with sqlite, then switched to postgres, and if you had created a superuser with the sqlite, then you need to add the superuser to the postgres instance, else you will not have entry to the admin page.


## Lesson 3. makemigrations
You make your models for the database in, you guessed it, the models.py file of your app. To apply the changes that you make in the models.py file, run ```python manage.py makemigrations appname```. Stuff that you create with makemigrations gets dummped into the, you guessed it, migrations directory.

You can check on what Django might do on the makemigrations command with ```python manage.py sqlmigrate```
