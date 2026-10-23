from django.urls import path
from . import views 


urlpatterns = [
    path('', views.books_list,name="books"),
    path('edit/<int:id>/', views.books_edit, name='book_edit'),
    path('delete/<int:id>/', views.books_delete, name='book_delete'),
]
