"""Forms for users in quiz_app"""

#django 
from django import forms
from django.contrib.auth.models import User

from user.models import Player

class SignupForm(forms.Form):
    """sing up form"""
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.PasswordInput()
    )
    confirmation_password = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name= forms.CharField(min_length=2,max_length=50)
    last_name= forms.CharField(min_length=2,max_length=50)
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """username mustbe unique"""

        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('El usuario ya existe.')
        return username
    def save(self):
        """Create and save user and Player"""
        data = self.cleaned_data
        data.pop('confirmation_password')

        user = User.objects.create_user(**data)
        player = Player(user=user)
        player.save()

class PlayerForm(forms.Form):
    """Player form """
    
    biography = forms.CharField(max_length=20,required=False)
    picture = forms.ImageField()

