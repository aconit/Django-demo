from django.urls import path
from . import views 


urlpatterns = [
    path('', views.users_list,name="users"),
    path('login/', views.users_login, name='login'),
    path('logout/', views.users_logout, name='logout'),
    path('edit/<int:id>/', views.users_edit, name='user_edit'),
    path('delete/<int:id>/', views.users_delete, name='user_delete'),
]
