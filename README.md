# To-do List

This is a very simple example of a to-do list, developed using Django2 and Python3.

## Prerequisites

- Virtualenv and pip
- Python 3.6.3
- Sqlite3

### Installing

A step by step to run and test on your local machine:

1. Create a virtualenv: virtualenv --python=python3 nameproject
2. Active virtual environment: cd nameproject && source bin/activate
3. Clone this repository
4. Install requirements: pip install -r requirements.txt
5. Create a .env file in root project with content: SECRET_KEY=secretkeyhere
6. Migrate database: python manage.py migrate
7. Create superuser: python manage.py createsuperuser
8. Run the server using 'python manage.py runserver'
9. Test on your browser: http://127.0.0.1:8000
