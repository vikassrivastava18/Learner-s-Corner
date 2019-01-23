from django.contrib import admin
from .models import Question, Topic, Answer
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ('question','asked_by','topic')
    list_filter = ('date',)
admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(Answer)
