# home_work_django

## 🗄️ PostgreSQL Database Configuration

To connect the project to a PostgreSQL database using `pg_service.conf` and `.pgpass`, follow these steps:

### 1. Update your `settings.py`:
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'service': 'my_service',
            'passfile': '.pgpass',
        },
    }
}

### Create the file ~/.pg_service.conf

['my_service']
host=localhost
port=5432
user=login_in DB
dbname=name_DB
#### Make sure the file has proper permissions:
chmod 600 ~/.pg_service.conf


### create the file .pgpass
in file write
localhost:5432:name_DB:login_in_DB::passwor_for_DB_user

###  Set permissions for .pgpass:
chmod 600 .pgpass

## Apply migrations
python manage.py makemigrations
python manage.py migrate

## Create superuser
python manage.py createsuperuser

## Project Structure
home_work_django/
├── manage.py
├── lesson_django/         # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── lesson_3/             # Your Django app
│   ├── models.py
│   ├── views.py
│   └── ...
|
└── README.md
