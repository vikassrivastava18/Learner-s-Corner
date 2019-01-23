from django.contrib import admin
from . models import Course, Notes, Subject, Question, Answer
# Register your models here.
admin.site.register(Course)
admin.site.register(Notes)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)