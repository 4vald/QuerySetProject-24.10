from django.urls import path
from . import views

urlpatterns = [
   path('', views.books_list, name='books_list'),
   path('add/', views.add_book, name='add_book'),
   path('edit/<int:id>/', views.edit_book, name='edit_book'),
   path('delete/<int:id>/', views.delete_book, name='delete_book'),

]

