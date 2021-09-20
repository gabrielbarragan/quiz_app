from django.contrib import admin
from .models import Question, Answer
# Register your models here.

class AnswerInline(admin.TabularInline):
    model= Answer
    list_display = ('pk','question','text','correct')
    readonly_fields = ('pk','question',)

class QuestionAdmin (admin.ModelAdmin):
    inlines=[AnswerInline]
    list_display = ('pk','text','quiz')
    readonly_fields = ('pk',)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)