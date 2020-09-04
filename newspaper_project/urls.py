"""newspaper_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',include('pages.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    # here we don't want to create a view for home so we use template view for shortcut
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('users.urls')), # this one is user for sign up which one we have to create
    path('users/',include('django.contrib.auth.urls')), # this one is use for django build in login,logout and password_change etc
    # usrs/login, users/logout, users/password_change, users/password_change/done, users/password_reset, users/password_reset/done these url don't need to create,django automatically build this url
    # for django.contrib.auth.urls
]
