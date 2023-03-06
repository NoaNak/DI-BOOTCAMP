from django.shortcuts import render
from django.http import HttpResponse


def some_text(request): 
    """Shows a text on screen inside browser"""
    return HttpResponse('SOME TEXT')

# Create your views here.
def about(request):
    return HttpResponse('HELLO WORLD')


def person_info(request, i:int):
    info = ['Yossi', 'Noa', 'Dalu', 'Elie']
    person = info[i]
    return HttpResponse(person)


def posts(request):
    author = 'Noa'
    title = 'My first post'
    body = 'Some text about my post etc'
    context: dict = {'author': author, 'title': title, 'body': body}
    # context - data that goes to html 
    # template = an html file

    return render(request, 'posts.html', context)


def profile(request):
    context = {
        'name': 'Noa Nakache',
        'age': 20,
        'gender': 'F',
        'hobbies': ['Python', 'Django', 'Html']
    }

    return render(request, 'profile_user.html', context)

