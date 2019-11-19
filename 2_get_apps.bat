REM Correr este script dentro del ambiente
REM Este script carga todas las aplicaciones y general la bd

python -m pip list
python -m pip install --upgrade pip
python -m pip install autopep8 django django-livereload-server django-extensions pydotplus pillow django-crispy-forms django-filter
python manage.py makemigrations
python manage.py migrate