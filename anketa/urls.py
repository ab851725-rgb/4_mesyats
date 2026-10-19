from django.urls import path
from .views import (
    AnketaListView,
    AnketaDetailView,
    AnketaCreateView,
    AnketaUpdateView,
    AnketaDeleteView,
)

urlpatterns = [
    path('anketas/', AnketaListView.as_view(), name='anketa_list'),
    path('anketas/create/', AnketaCreateView.as_view(), name='anketa_create'),
    path('anketas/<int:id>/', AnketaDetailView.as_view(), name='anketa_detail'),
    path('anketas/<int:id>/update/', AnketaUpdateView.as_view(), name='anketa_update'),
    path('anketas/<int:id>/delete/', AnketaDeleteView.as_view(), name='anketa_delete'),
]