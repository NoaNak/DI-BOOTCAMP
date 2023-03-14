from django.contrib import admin
from django.urls import path
from films.views import add_film, add_director, homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_film/', add_film, name='add_film'), 
    path('add_director/', add_director, name='add_director'),
    path('homepage/', homepage, name='homepage')
]
