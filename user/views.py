"""Users View"""

from django.shortcuts import render
from django.contrib.auth import views as auth_views
# Create your views here.

#models

from user.models import User, Player
class LoginView(auth_views.LoginView):
    """Login user view"""
    
    template_name = 'user/login.html'