from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    RegisterView,
    CineLoginView,
    CineLogoutView,
    AddCommentView,
    BookVipSeatView,
)

urlpatterns = [
    path('cineboard/', MovieListView.as_view(), name='movie_list'),
    path('cineboard/create/', MovieCreateView.as_view(), name='movie_create'),
    path('cineboard/<int:id>/', MovieDetailView.as_view(), name='movie_detail'),
    path('cineboard/<int:id>/update/', MovieUpdateView.as_view(), name='movie_update'),
    path('cineboard/<int:id>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('cineboard/<int:id>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('cineboard/<int:id>/vip/', BookVipSeatView.as_view(), name='book_vip_seat'),
    path('cineboard/register/', RegisterView.as_view(), name='cineboard_register'),
    path('cineboard/login/', CineLoginView.as_view(), name='cineboard_login'),
    path('cineboard/logout/', CineLogoutView.as_view(), name='cineboard_logout'),
]