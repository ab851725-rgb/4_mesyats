from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from .models import Book

def book_list_view(request):
    search_query = request.GET.get('q', '')
    if search_query:
        book_list = Book.objects.filter(title__icontains=search_query).order_by('-id')
    else:
        book_list = Book.objects.all().order_by('-id')

    paginator = Paginator(book_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'books': page_obj,
        'search_query': search_query,
    }
    return render(request, 'book/book_list.html', context)

def book_detail_view(request, id):
    book = get_object_or_404(Book, id=id)
    book.views_count += 1
    book.save()
    return render(request, 'book/book_detail.html', {'book': book})

def favourite_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('Пушкин')

def facts_about_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('красиво писал, был убит как гангстер в перестрелке, но не факт ведь потом появился Александр Дюма, который писал таким же слогом, и в общем его работы были крайне схожи')

def my_opinion_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('мое мнение таково, что это одна из самых значительных фигур в поэзии того времени')