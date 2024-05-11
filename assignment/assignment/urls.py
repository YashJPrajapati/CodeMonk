"""
URL configuration for assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
