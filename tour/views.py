from django.views.generic import ListView, DetailView
from .models import Tour

class TourListView(ListView):
    model = Tour
    template_name = 'tour/tour_list.html'
    context_object_name = 'tours'

class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour/tour_detail.html'
    context_object_name = 'tour'
    pk_url_kwarg = 'id'