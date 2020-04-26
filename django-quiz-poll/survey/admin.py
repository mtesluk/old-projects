from django.contrib import admin
from .models import Question, Category, Topic, Answer
# Register your models here.

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(Category)
