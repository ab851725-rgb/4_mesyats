from django.urls import path
from .views import (
    book_list_view, 
    book_detail_view, 
    favourite_writer_view, 
    facts_about_writer_view, 
    my_opinion_writer_view,
)

urlpatterns = [
    path('books/', book_list_view, name='book_list'),
    path('books/<int:id>/', book_detail_view, name='book_detail'),
    path('favourite_writer/', favourite_writer_view),
    path('facts_about_writer/', facts_about_writer_view),
    path('my_opinion_writer/', my_opinion_writer_view)
]