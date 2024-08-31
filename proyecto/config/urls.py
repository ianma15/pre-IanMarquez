"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from universidad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('estudiante/list/', views.estudiante_list, name="estudiante_list"),
    path('materia/list/', views.materia_list, name="materia_list"),
    path('solicitud/list/', views.solicitud_list, name="solicitud_list"),
    path('estudiante/create/', views.estudiante_create, name="estudiante_create"),
    path('materia/create/', views.materia_create, name="materia_create"),
    path('solicitud/create/', views.solicitud_create, name="solicitud_create"),
]
