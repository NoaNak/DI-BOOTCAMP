from django.shortcuts import render
from .models import Person

def find_by_number(request, phonenumber:str):
    person = Person.objects.get(phone_number=phonenumber)
    context = {'person': person}
    return render(request, 'person.html', context)

def find_by_name(request, name:str):
    person = Person.objects.get(name=name.capitalize())
    context = {'person': person}
    return render(request, 'person.html', context)