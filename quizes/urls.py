from django.urls import path
from .views import (
    QuizListView,
    QuizDetailView
)

app_name='quizes'

urlpatterns = [
    path(
        route='',
        view= QuizListView.as_view(), 
        name='main-view'
        ),
    path(
        route='<str:quiz_id>/',
        view=QuizDetailView.as_view(), 
        name='quiz-view'
        ),
]