from django.shortcuts import render, redirect
from .forms import AddFilmForm, AddDirectorForm
from .models import Film

# Create your views here.


def add_film(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_film')
    else:
        form = AddFilmForm()
    return render(request, 'addFilm.html', {'form': form})

def add_director(request):
    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_director')
    else:
        form = AddDirectorForm()
    return render(request, 'addDirector.html', {'form': form})

def homepage(request):
    films = Film.objects.all()
    context = {
        'films':films
    }
    return render(request, 'homepage.html', context)