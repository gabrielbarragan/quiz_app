"""quiz_app middleware"""

from django.shortcuts import redirect
from django.urls import reverse

from user import urls
from user.models import Player
from django.core.exceptions import ObjectDoesNotExist

class UserIsAuthenticatedMiddleware:
    """User is authenticated middleware
    Ensure that user authenticated do not use the login access template 
    """
    def __init__(self,get_response):
        """middleware initialization"""
        self.get_response= get_response

    def __call__(self,request):
        """code to be executed for each request before the view is called"""

        if not request.user.is_anonymous:
            if request.path in [reverse('user:login')]:
                return redirect('quizes:main-view')
        response = self.get_response(request)
        return response
