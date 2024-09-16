1. create virtual env
virtualenv venv

2. activate virtual environment
source venv/bin/activate

3. Install Django and Django Rest Framework
pip install django djangorestframework

4. Create a New Django Project
django-admin startproject todo_project .

5. Create the To-Do App
python manage.py startapp todo

6. Add Your App and DRF to Installed Apps

7.  Defining the ToDo Model

8. Creating a Serializer. create a serializers.py file inside the app folder. A serializer converts data between different formats (like Python objects to JSON, and vice versa). This is important for APIs, which exchange data in formats like JSON

9. Defining API Views in your views.py file