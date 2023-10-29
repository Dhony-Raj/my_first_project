"""
URL configuration for fms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from . import views as v
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', v.flat, name='home'),
    path('index/', v.input, name='flat_creation'),
    path('Flat_edit/<int:id>', v.update, name='edit_flat_index'),
    path('Flat_update/', v.update1, name='flat_update'),
    path('delete_flat/<slug:id>', v.delete_flat, name='delete_flat_index'),
]
