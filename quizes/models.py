from django.db import models
import random

# Create your models here.

DIFF_CHOICES = (
    ('fácil', 'fácil'),
    ('medio','medio'),
    ('alta','alta'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duración en minutos")
    required_score_to_pass = models.IntegerField(help_text="puntaje requerido en %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f'{self.topic} - {self.pk} - {self.topic}'
    
    def get_questions(self):
        questions = list(self.question_set.all()) #crea una lista con todas las preguntas
        random.shuffle(questions)#reordena la lista aleatoriamente
        return questions[:self.number_of_questions] #selecciona las primeras preguntas según la cantidad de preguntas que se asignen al quiz y definidas en number_of_questions

    class Meta:
        verbose_name_plural= 'Quizes'