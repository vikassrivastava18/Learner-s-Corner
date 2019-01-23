from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.study, name='study'),
    path('course/<course>',views.courses, name='courses'),
    path('course/ajax/save_notes/',views.save_notes, name='save_notes'),
    path('course/ajax/ask_question/',views.question,name='question')
    ]




