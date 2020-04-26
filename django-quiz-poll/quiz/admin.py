from django.contrib import admin
from .models import Category, Topic, Question, Answer


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']

    inlines = [AnswerInline]


class BaseAdmin(admin.ModelAdmin):
    search_fields = ['name']

    inlines = [QuestionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic)
admin.site.register(Answer)
admin.site.register(Category)
