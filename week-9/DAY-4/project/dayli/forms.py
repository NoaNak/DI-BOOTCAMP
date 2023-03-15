from django import forms
from .models import Daily

class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ('__all__')
        widgets = { "name": forms.Textarea(attrs={'class':'name'}), 
                   "adress": forms.Textarea(attrs={'class':'adress'}), 
                   "city": forms.Textarea(attrs={'class':'city'}), 
                   'country': forms.Textarea(attrs={'class':'country'}) 
                   }


