"""Users View"""

from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse, reverse_lazy

#models
from user.models import User, Player

#forms
from user.forms import SignupForm

# Create your views here.
class LoginView(auth_views.LoginView):
    """Login user view"""
    
    template_name = 'user/login.html'

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Users Logout view"""
    next_page= 'user:login'

class SignupView(FormView):
    """user signup view"""
    form_class = SignupForm
    template_name = 'user/new_user.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        """save form data"""
        form.save()

        return super().form_valid(form)
