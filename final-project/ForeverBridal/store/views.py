from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'index.html')

def login(request):
    return render (request, 'login.html')

def signin(request):
    return render (request, 'signin.html')

def forget_password(request):
    return render (request, 'forget-password.html')

def contact(request):
    return render (request, 'contact.html')

def dress(request):
    return render (request, 'dress.html')
    
def manSuit(request):
    return render (request, 'manSuit.html') 
   
def accessories(request):
    return render (request, 'accessories.html')

def manAccessories(request):
    return render (request, 'manAccessories.html')

def earring(request):
    return render (request, 'earring.html')