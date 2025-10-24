from django.urls import path
from . import  views

urlpatterns = [
    path('books/', views.books_view, name='books'),
    path('search/', views.search_view, name='search')
]
