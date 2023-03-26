from django.contrib import admin
from django.urls import path
from films.views import add_film, add_director, homepage
from accounts.views import (IMDBLoginView, IMDBLogoutView, RegisterView, ProfileCreateView, ProfileView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_film/', add_film, name='add_film'), 
    path('add_director/', add_director, name='add_director'),
    path('homepage/', homepage, name='homepage'),
    path('login/', IMDBLoginView.as_view(), name='login'),
    path('logout/', IMDBLogoutView.as_view(), name='logout'),
    path('Register/', RegisterView.as_view(), name='register'),
    path('Profile_create/', ProfileCreateView.as_view(), name='profile'),
    path('ProfileView/', ProfileView.as_view(), name='profile')
]
