from django.shortcuts import render
from django.contrib.auth.views import LoginView
# Create your views here.


class IMDBLoginView(LoginView):
    template_name = 'login.html'

class IMDBLogoutView(LoginView):
    template_name = 'logout.html'