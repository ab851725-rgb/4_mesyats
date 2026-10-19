from django.views.generic import ListView, DetailView, View
from django.shortcuts import HttpResponse
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Book.objects.filter(title__icontains=query).order_by('-id')
        return Book.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save()
        return obj

class FavouriteWriterView(View):
    def get(self, request):
        return HttpResponse('Пушкин')

class FactsAboutWriterView(View):
    def get(self, request):
        return HttpResponse('красиво писал, был убит как гангстер в перестрелке, но не факт ведь потом появился Александр Дюма, который писал таким же слогом, и в общем его работы были крайне схожи')

class MyOpinionWriterView(View):
    def get(self, request):
        return HttpResponse('мое мнение таково, что это одна из самых значительных фигур в поэзии того времени')