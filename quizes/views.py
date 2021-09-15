from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView, DetailView

# Create your views here.

class QuizListView (ListView):
    '''Quiz view'''
    model = Quiz
    template_name = 'quizes/main.html'
    context_object_name= 'quizes'

class QuizDetailView(DetailView):
    """User detail view."""
	
    template_name='quizes/quiz.html'
    slug_field= 'pk'
    slug_url_kwarg='quiz_id'
    queryset = Quiz.objects.all()

    context_object_name = 'quiz'

#sin usar por ahora
