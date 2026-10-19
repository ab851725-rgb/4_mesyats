from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    FavouriteWriterView,
    FactsAboutWriterView,
    MyOpinionWriterView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('favourite_writer/', FavouriteWriterView.as_view()),
    path('facts_about_writer/', FactsAboutWriterView.as_view()),
    path('my_opinion_writer/', MyOpinionWriterView.as_view()),
]