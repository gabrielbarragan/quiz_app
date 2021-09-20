from django.urls import path
from .views import (
    QuizListView,
    QuizDetailView,
    QuizDataView,
    save_quiz_view
    
)

app_name='quizes'

urlpatterns = [
    path(
        route='',
        view= QuizListView.as_view(), 
        name='main-view'
        ),
    path(
        route='<int:quiz_id>/',
        view=QuizDetailView.as_view(), 
        name='quiz-view'
        ),
    path(
        route='<int:quiz_id>/data/',
        view=QuizDataView.as_view(), 
        name='quiz-data-view'
        ),
    path(
        route='<int:quiz_id>/save/',
        view=save_quiz_view, 
        name='quiz-save-view',
        ),
]