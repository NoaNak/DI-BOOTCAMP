from django.shortcuts import render
import json

# Create your views here.

def read_data():
    filename = 'data.json'

    with open(filename, 'r') as file:
        data = json.load(file)

    return data

def family_list(request):

    data = read_data()
    context = {'families': data['families']}

    return render(request, 'families.html', context)  

def animal(request, id:int):

    data = read_data()
    animal_list = data['animals']
    animal = animal_list[id-1]

    context = {'animal': animal}

    return render(request, 'animal.html', context)