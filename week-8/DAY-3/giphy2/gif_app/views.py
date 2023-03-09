from django.shortcuts import render
from .models import Category, Gif
from .forms import CategoryForm, GifForm

# Create your views here.

def homepage(request):

    if request.method == 'POST':
        form = GifForm(request.POST)
        form.save()

    gifs_all = Gif.objects.all()
    context = {'gifs': gifs_all, "form": form}

    return render(request, 'homepage.html', context)

def category(request, id:int):

    category_specific = Category.objects.get(id=id)
    category_gifs = category_specific.gifs.all()

    context = {'category': category_specific, 'gifs': category_gifs}

    return render(request, 'category.html', context)

def categories(request):
    
    # Request methods
    # GET - getting data
    # POST - changing data

    if request.method == 'POST':
         print("DATA POST:", request.POST)
         form = CategoryForm(request.POST) # after data in form
         form.save()
    
    categories_all = Category.objects.all()
    form = CategoryForm() # empty form 
    context = {'categories': categories_all, 'form': form}

    return render(request, 'categories.html', context)