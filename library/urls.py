from django.urls import path

from . import views


urlpatterns = [
    path('', views.library, name='library'),
    path('<genre>/', views.book_by_genre, name='book_by_genre'),
    path('book_detail/<isbn>/', views.book_detail, name='book_detail'),
]
