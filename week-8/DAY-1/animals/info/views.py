from django.shortcuts import render
from .models import Family, Animal


def animals_list(request):
    animals = Animal.objects.all().order_by('name') # to order all the animals by their name field
    context = {'animals': animals}

    return render(request, 'animals.html', context)


def family_list(request):
    families = Family.objects.all()
    context = {'families': families}

    return render(request, 'families.html', context)

def animal(request, id:int): 
    animal_specific = Animal.objects.get(id=id)
    context = {'animal': animal_specific}

    return render(request, 'animal.html', context)

def family(request, id:int):
    family_specific = Family.objects.get(id=id)
    family_animals = family_specific.animal_set.all()
    count = family_animals.count() # count how many objects 

    context = {'family': family_specific, 'animals': family_animals, 'count': count}

    return render(request, 'family.html', context)