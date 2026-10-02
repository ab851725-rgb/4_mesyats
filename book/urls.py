from django.urls import path
from .views import book_list_view, book_detail_view

urlpatterns = [
    path('books/', book_list_view, name='book_list'),
    path('books/<int:id>/', book_detail_view, name='book_detail'),
]