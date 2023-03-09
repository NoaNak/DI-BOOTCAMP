from django import forms
from .models import Category, Gif

class CategoryForm(forms.ModelForm): # ModelForm is a form with connection to a 
                                    # specific model

    class Meta:
        model = Category # the model of the form
        fields = ('__all__') # the fields of the model 

class GitForm(forms.ModelsForm):

    class Meta:
        model = Gif
        fields = ('__all__')