from django.urls import path
from articles import views


urlpatterns = [
    path('',views.article,name='article'),
    path('article_detail/<id>',views.article_detail,name='article_detail'),
    path('write_article',views.write_article,name='write_article')
]
