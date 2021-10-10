
#django
from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

#models
from .models import Quiz
from results.models import Result
from questions.models import Question, Answer



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

class QuizListView (LoginRequiredMixin, ListView):
    '''Quiz list view'''
    model = Quiz
    template_name = 'quizes/main.html'
    context_object_name= 'quizes'

class QuizDetailView(LoginRequiredMixin, DetailView):
    """Quiz detail view."""
	
    template_name='quizes/quiz.html'
    slug_field= 'pk'
    slug_url_kwarg='quiz_id'
    model= Quiz
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

def save_quiz_view(request,quiz_id):
    if request.is_ajax():
        
        answers=[]
        data = request.POST
        data_=dict(data)
        
        data_.pop('csrfmiddlewaretoken')
        data_.pop('quiz_name')
        data_.pop('n_question')

        score=0
        user= request.user
        quiz = Quiz.objects.get(name=data['quiz_name'])
        n_question= data['n_question']
        multiplier= 100/int(n_question)

        correct=''
        
        for key,values in data_.items():
            
            q=Question.objects.get(pk=key)

            for ans in q.get_answer():
                if ans.correct==True:
                    correct=ans.text

            if values[0] != '':
                answer= Answer.objects.get(pk=values[0])
                answered=answer.text

                if answer.correct == True:
                    score += 1 * multiplier 

            elif values[0] =='':
                answered='not answered'

            answers.append({str(q):{'correct_answer': correct, 'answered':answered }})
        Result.objects.create(quiz=quiz, user=user, score= score)

        if score >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score':score, 'results': answers})
        else:
            return JsonResponse({'passed': False, 'score':score, 'results': answers})

    return HttpResponse({'text':'works'})


    



        
        

        

