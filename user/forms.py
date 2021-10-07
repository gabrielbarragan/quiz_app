"""Forms for users in quiz_app"""

#django 
from django import forms
from django.contrib.auth.models import User

from user.models import Player

class PlayerForm(forms.Form):
    
    biography = forms.CharField(max_length=500,required=False)
    picture = forms.ImageField()