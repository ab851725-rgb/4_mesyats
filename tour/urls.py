from django.urls import path
from .views import tour_list_view, tour_detail_view

urlpatterns = [
    path('tours/', tour_list_view, name='tour_list'),
    path('tours/<int:id>/', tour_detail_view, name='tour_detail'),
]