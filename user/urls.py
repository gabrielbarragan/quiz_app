"""Users urls"""

#Django

from django.urls import path

#view
from user import views

urlpatterns =[
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    )
]