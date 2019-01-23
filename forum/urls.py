from django.urls import path

from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('answerdetails/<id>', views.answerdetails, name='answerdetails'),
    path('answerdetails/ajax/resolved/', views.resolved, name='resolved')
]
