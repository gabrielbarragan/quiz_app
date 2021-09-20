"""Results Form"""
#django
from django import forms
from django.contrib.auth.models import User

#models
from .models import Result
from quizes.models import Quiz

class CreateResultForm(forms.Form):
    """result create form"""
    quiz = forms.CharField(min_length=4,max_length=20)
    user = forms.CharField(min_length=4, max_length=50)
    score = forms.FloatField()

    def save(self):
        """Create and save user and profile"""
        data = super().clean()
        user= self.data['username']
        quiz= self.data['quiz']
        quiz_taken= Quiz.objects.filter(name=quiz).exists()
        if not quiz_taken:
            raise forms.ValidationError('quiz no existe')        
        score= self.data['score']

        result=Quiz(quiz=quiz,user=user,score=score)
        result.save()


