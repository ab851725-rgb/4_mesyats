from django.shortcuts import render, get_object_or_404, HttpResponse
from . models import Book


def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail_view(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book/book_detail.html', {'book': book})

def favourite_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('Пушкин')

def facts_about_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('красиво писал, был убит как гангстер в перестрелке,' \
        ' но не факт ведь потом появился Александ Дюма, который писал таким же слогом,' \
        ' и в общем его работы были карйне схожи'
        )

def my_opinion_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('мое мнение таково, что это одна из самых значительных фигур в поэзии того времени')