from django.shortcuts import render, redirect
from django.urls import reverse
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

# pour faire d'une maniere differente:
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from .models import Film, Director, Category
# from .forms import AddDirectorForm, AddFilmForm
# from django.views.generic import FormView, ListView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView


# class AddCategoryView(CreateView):
#     model = Category
#     template_name = 'add_category.html'
#     fields = '__all__'
#     def get_success_url(self) -> str:
#         return reverse('add_film')
    
# class DeleteCategoryView(DeleteView):
#     model = Category
#     template_name = 'delete_category.html'
#     fields = '__all__'
#     def get_success_url(self) -> str:
#         return reverse('add_film')

# class UpdateCategoryView(UpdateView):
#     model = Category
#     template_name = 'update_category.html'
#     fields = '__all__'
#     def get_success_url(self) -> str:
#         return reverse('add_film')


# class FilmListView(ListView):
#     template_name = 'films.html'
#     model = Film
#     context_object_name = 'films'

# class AddFilmView(FormView):
#     template_name = 'add_film.html'
#     form_class = AddFilmForm

#     def get_success_url(self) -> str:
#         return reverse('films')
    
#     def form_valid(self, form): # runs when submit button clicked
#         form.save()
#         return super().form_valid(form)

# def add_director(request):

#     errors = {}

#     if request.method == 'POST':
#         form = AddDirectorForm(request.POST)
#         if form.is_valid(): # checks that the data is ok
#             form.save()
#             return redirect('directors') # redirects to the directors page
#         else:
#             errors = form.errors

#     form = AddDirectorForm()
#     context = {'form': form, 'errors': errors}
#     return render(request, 'add_director.html', context)



# class DirectorListView(ListView):
#     model = Director
#     template_name = 'directors.html'
#     context_object_name = 'directors'