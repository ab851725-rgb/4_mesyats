from django.urls import path
from .views import (
    anketa_list_view,
    anketa_detail_view,
    anketa_create_view,
    anketa_update_view,
    anketa_delete_view,
)

urlpatterns = [
    path('anketas/', anketa_list_view, name='anketa_list'),
    path('anketas/create/', anketa_create_view, name='anketa_create'),
    path('anketas/<int:id>/', anketa_detail_view, name='anketa_detail'),
    path('anketas/<int:id>/update/', anketa_update_view, name='anketa_update'),
    path('anketas/<int:id>/delete/', anketa_delete_view, name='anketa_delete'),
]