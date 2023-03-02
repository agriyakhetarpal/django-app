# Instructions

It is recommended to use a virtual environment. To use this app, run

```
# in the djangoform/ directory
python manage.py makemigrations djangoform
```

and then migrate and run the app
```
python manage.py migrate
```

```
python manage.py runserver
```

and navigate to [http:127.0.1:8000/contact](http:127.0.1:8000/contact) to access the form. The details will get stored in the `djangoform_contact` table.
