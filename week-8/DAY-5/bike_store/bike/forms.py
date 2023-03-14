from django import forms 
from .models import Customer, Rental

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('__all__')
        # exclude = ('country', )

class RentalForm(forms.ModelForm):
    class Meta: # class for specifying crucial things like the model and the fields that the form uses 
        model = Rental
        fields = '__all__'
