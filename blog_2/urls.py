from django.urls import path
from .views import (
    HelloWorldView,
    MyFavouriteEmojiView,
    AboutMySelfView,
    MyFavouriteWriterView,
    FactsAboutWriterView,
    MyOpinionWriterView,
)

urlpatterns = [
    path('hello_world/', HelloWorldView.as_view()),
    path('favorite_emoji/', MyFavouriteEmojiView.as_view()),
    path('me/', AboutMySelfView.as_view()),
    path('favourite_writer/', MyFavouriteWriterView.as_view()),
    path('facts_about_writer/', FactsAboutWriterView.as_view()),
    path('my_opinion_writer/', MyOpinionWriterView.as_view()),
]