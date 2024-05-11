# Django Documentaion

## Installation SetUp

Make sure you refer to the django version you are using. A quick way to start a new django project is to run the
following command:
* Create One Folder Name it As CodeMonk as a BaseDirectory
* Open the Folder in the Address bar(path) cmd --> code . it will open VS Code
* Open the new terminal Performe the following steps in the terminal:
*
  1. Virtual environment: Creating Virtual Environment in Python.
     ```shell
     python -m venv myenv
     ```
  2. Activate the virtual environment:
     ```shell
     myenv\Scripts\activate
     ```
  3. Django: Web framework for building web applications in Python.
     ```shell
     pip install django
     ```
  4. Django REST Framework: Toolkit for building Web APIs in Django.
     ```shell
     pip install django djangorestframework
     ```
  5. PyJWT: Library for encoding and decoding JSON Web Tokens (JWT)
     ```shell
     pip install PyJWT
     ```
  6. psycopg2: PostgreSQL adapter for Python.
     ```shell
     pip install psycopg2
     ```
  7. psycopg2-binary: Binary package for psycopg2, an adapter for PostgreSQL.
     ```shell
     pip install psycopg2-binary
     ```
  8. pytz: Library for working with timezones in Python.
     ```shell
     pip install pytz
     ```
  9. sqlparse: Non-validating SQL parser for Python.
     ```shell
     pip install sqlparse
     ```
10. tzdata: Library for time zone data.
     ```shell
     pip install tzdata
     ```
11. asgiref: ASGI framework reference implementation, required by Django channels.
     ```shell
     pip install asgiref
     ```

* Go to your desired development folder and create a new django project:

```shell
django-admin startproject assignment
```

* Go to the new create django project:

```shell
cd assignment
```



* Install  Requirements

```shell script
pip install requirements.txt
```

* create a new django App:

```shell
python manage.py startproject paragraph
```

* Add Books to INSTALLED_APPS in you new Django Project.

```python
INSTALLED_APPS = [
    ...,
    'paragraph',
    ...,
]
```

* Perform database migrations:

```shell
python manage.py makemigrations
python manage.py migrate
```

* Run your project:

```shell
python manage.py runserver
```

* Navigate to Project root view assigned in your project urlpatterns setting (typically http://127.0.0.1:8000/
if you followed this installation guide).
* Use your superuser credentials to login.


# Django REST Framework Documentaion

# API Setup

Official Django REST framework documentation: https://www.django-rest-framework.org/

The Django REST framework is a powerful and flexible toolkit for building web APIs in Django applications. It provides a set of utilities and serializers to easily create RESTful APIs that can handle various data formats, authentication, permissions, and more.

The documentation covers all aspects of DRF, including installation, configuration, serializers, views, authentication, permissions, pagination, versioning, filtering, and more. It's a comprehensive resource that helps developers understand and leverage the features provided by DRF efficiently.

* Install Django REST framework:

```shell
pip install django djangorestframework
```

* Add Django REST framework to your Django project:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...,
]
```

* Include your API URLs in the project's URL configuration:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app.urls')),  # Include your app's API URLs
]
```



* Access the API documentation:
    With the above steps completed, you can now access the API documentation in your browser. Open your web browser and navigate to:

URL :   http://127.0.0.1:8000/


Assuming you are running your development server on the default port (8000).
You should see an interactive API documentation page showing your API endpoints, their methods (GET, POST, etc.), and the parameters they accept. The browsable API documentation allows you to test your API endpoints directly from the browser, making it convenient for both development and exploration.

# API Documentation
https://github.com/YashJPrajapati/Backend-Developer-Assignment/blob/main/API_Documentaion.md

# Screenshots
