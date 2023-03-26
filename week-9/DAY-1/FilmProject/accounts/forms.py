from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
        # exclude = ('user',)
        widgets = {
            'user': forms.HiddenInput(),
            'favorite_films': forms.Select(attrs={"class": "fav_films"}),
            'favorite_directors': forms.Select(attrs={"class": "fav_directors"}),
            'favorite_categories':forms.Select(attrs={"class": "fav_categories"})
        }

def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["user"].label = ""