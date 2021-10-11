"""Users View"""

from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse, reverse_lazy

#models
from user.models import User, Player
from results.models import Result

#forms
from user.forms import SignupForm

# Create your views here.
class LoginView(auth_views.LoginView):
    """Login user view"""
    
    template_name = 'user/login.html'
    next_url= 'user/me/profile'

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

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""
	
    template_name='user/detail.html'
    slug_field= 'username'
    slug_url_kwarg='username'
    queryset = User.objects.all()

    context_object_name = 'user'

    def get_context_data(self,**kwargs):
        """Add user's results to context"""

        context = super().get_context_data(**kwargs)
        user = self.get_object()
        query= Result.objects.filter(user=user).order_by('-score')
        context['results']= query[:4]

        return context

class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user/update_player.html'
    model = Player
    fields = ['biography', 'picture']

    def get_object(self):
        """return user's Player profile"""
        return self.request.user.player

    def get_success_url(self):
        """return to user's Player profile"""

        username = self.object.user.username
        return reverse('user:detail', kwargs={'username':username})
