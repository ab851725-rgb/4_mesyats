from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Anketa
from .forms import AnketaForm

class AnketaListView(ListView):
    model = Anketa
    template_name = 'anketa/anketa_list.html'
    context_object_name = 'anketas'
    ordering = ['-created_at']

class AnketaDetailView(DetailView):
    model = Anketa
    template_name = 'anketa/anketa_detail.html'
    context_object_name = 'anketa'
    pk_url_kwarg = 'id'

class AnketaCreateView(CreateView):
    model = Anketa
    form_class = AnketaForm
    template_name = 'anketa/anketa_create.html'
    success_url = reverse_lazy('anketa_list')

class AnketaUpdateView(UpdateView):
    model = Anketa
    form_class = AnketaForm
    template_name = 'anketa/anketa_update.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('anketa_detail', kwargs={'id': self.object.id})

class AnketaDeleteView(DeleteView):
    model = Anketa
    template_name = 'anketa/anketa_delete_confirm.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('anketa_list')