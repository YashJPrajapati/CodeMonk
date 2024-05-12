# Django Documentaion

## Basic Setup:
* 1. Create a folder as your workplace
  2. Create a django project with name using
     ```shell
     django-admin startproject your_projectname
     ```
  3. Move to the directoy by using
    ```shell
    cd your_projectname
    ```
  4. Create a application with a name
     ```shell
     python manage.py your_appname
     ```
  5. Create an virtual Environment so your Main system doen't get affected due to any install for the project
  6. Active the Script of venv drag and drop the Activate.ps1 file from myenv\Scripts\Activate.ps1 or
     ```shell
     myenv\Scripts\activate
     ```
  7. Edit the files and add the required file in the application and project

## Installation SetUp

Make sure you refer to the django version you are using. A quick way to start a new django project is to run the
following command:
* Create One Folder Name it As CodeMonk as a BaseDirectory
* Open the Folder in the Address bar(path) type cmd --> code . this will open VS Code
* Open the new terminal Performe the following steps in the terminal:
* 1. Virtual environment: Creating Virtual Environment in Python.
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

* Add App to INSTALLED_APPS in you new Django Project.

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
* NOTE: Weare going to use SMTP Method for sending email so make sure youn have created App Password for it.
  Follow the link to create app password: https://github.com/YashJPrajapati/CodeMonk/blob/main/App_Password.md
* Navigate to Project root view assigned in your project urlpatterns setting (typically http://127.0.0.1:8000/

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
from django.urls import path
from paragraph.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', signup.as_view(), name='signup'),
    path('sign_in/', signin.as_view(), name='signin'),
    path('createpara/', ParagraphAPI.as_view(), name='para'),
    path('createparalist/', Createwithlist.as_view(), name='paralist'),    
    path('createwithfile/', Createwithfile.as_view(), name='file'),    
    path('search/', SearchAPI.as_view(), name='search'), 
    path('modify/', Modifyuser.as_view(), name='modify'), 
    path('sign_out/', signout.as_view(), name='signout'),
]
```

* Include your API views in the App's Views.py
     ** Access the view.py file from the ripository 
          https://github.com/YashJPrajapati/CodeMonk/blob/main/assignment/paragraph/views.py



# API Documentation
https://github.com/YashJPrajapati/CodeMonk/blob/main/API_Documentaion.md

* Access the API documentation:
    With the above steps completed, you can now access the API documentation in your browser. Open your web browser and navigate to:
    * URL :   http://127.0.0.1:8000/

Assuming you are running your development server on the default port (8000).
You should see an interactive API documentation page showing your API endpoints, their methods (GET, POST, etc.), and the parameters they accept. The browsable API documentation allows you to test your API endpoints directly from the browser, making it convenient for both development and exploration.
