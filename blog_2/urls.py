from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.hello_world_view),
    path('favorite_emoji/', views.my_favourite_emoji_view),
    path('me/', views.about_my_self_view),
    path('favourite_writer/', views.my_favourite_writer_viev),
    path('facts_about_writer/', views.facts_about_writer_view),
    path('my_opinion_writer/', views.my_opinion_about_writer_view)
    ]


