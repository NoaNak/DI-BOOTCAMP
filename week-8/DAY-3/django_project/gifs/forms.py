from django import forms
from .models import Category

class CategoryForm(forms.ModelForm): # ModelForm is a form with connection to a 
                                    # specific model

    class Meta:
        model = Category # the model of the form
        fields = ('__all__') # the fields of the model 