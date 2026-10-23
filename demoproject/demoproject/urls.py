from django.contrib import admin
from django.urls import path, include
from books import views as books_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books_views.books_list),
    path('books/', include('books.urls')),
    path('users/', include('users.urls'))
]
