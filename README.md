# Django countdown timer
A simple countdown timer created in django using pure vanilla javascript.

## Local usage:
1.  Clone the repository 
```
git clone https://github.com/suravshrestha/django-countdown-timer.git
```

2.  Navigate to the project directory :open_file_folder:
```
cd django-countdown-timer
```

3.  Create a virtual environment
```
python -m venv venv
```

4.  Activate the virtual environment
```
.\venv\Scripts\activate
```

5.  Install the dependencies
```
pip install -r requirements.txt
```

6. Make migrations and migrate
```
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser to handle the database and admin panel
```
python manage.py createsuperuser
```

8. Start the development server
```
python manage.py runserver
```

9. Open your browser and go to your local domain `http://127.0.0.1:8000`
