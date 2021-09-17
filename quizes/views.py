from django.shortcuts import render

from .models import Quiz
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

# Create your views here.

class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context

class QuizListView (ListView):
    '''Quiz list view'''
    model = Quiz
    template_name = 'quizes/main.html'
    context_object_name= 'quizes'

class QuizDetailView(DetailView):
    """Quiz detail view."""
	
    template_name='quizes/quiz.html'
    slug_field= 'pk'
    slug_url_kwarg='quiz_id'
    queryset = Quiz.objects.all()

    context_object_name = 'quiz'

class QuizDataView(JSONResponseMixin, DetailView):
    """Quiz data view."""
    template_name='quizes/quiz_data.html'
    slug_field= 'pk'
    slug_url_kwarg='quiz_id'
    queryset = Quiz.objects.all()

    context_object_name = 'quiz_data'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        questions={}
        for q in context['object'].get_questions():
            answers=[]
            for a in q.get_answer():
                answers.append(a.text)
            questions[str(q)]= answers
        
        quiz_data= {
            'data':questions,
            'time':context['object'].time
            }

        return self.render_to_json_response(quiz_data)



    



        
        

        

