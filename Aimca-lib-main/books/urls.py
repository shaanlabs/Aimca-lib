from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/lend/', views.lend_book, name='lend_book'),
    path('books/lent/', views.lent_books, name='lent_books'),
    path('books/return/', views.return_book, name='return_book'),
    path('books/overdue/', views.overdue_books, name='overdue_books'),
    path('books/process-return/<int:loan_id>/', views.process_return, name='process_return'),
    path('about/', views.about_us, name='about_us'),
    path('api/books/', views.book_api, name='book_api'),
]