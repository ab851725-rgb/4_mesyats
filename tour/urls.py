from django.urls import path
from .views import TourListView, TourDetailView

urlpatterns = [
    path('tours/', TourListView.as_view(), name='tour_list'),
    path('tours/<int:id>/', TourDetailView.as_view(), name='tour_detail'),
]