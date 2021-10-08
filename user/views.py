"""Users View"""

from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#models

from user.models import User, Player
class LoginView(auth_views.LoginView):
    """Login user view"""
    
    template_name = 'user/login.html'

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Users Logout view"""
    next_page= 'user:login'