from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('add/', views.add_member, name='add_member'),
    path('<int:pk>/edit/', views.edit_member, name='edit_member'),
    path('<int:pk>/delete/', views.delete_member, name='delete_member'),
] 