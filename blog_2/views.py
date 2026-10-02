from django.shortcuts import render
from django.http import HttpResponse

def hello_world_view(request):
    if request.method == 'GET':
        return HttpResponse('это второй')

def my_favourite_emoji_view(reqest):
    if reqest.method == 'GET':
        return HttpResponse('🟢🟤🔵⚪⚫🟠')

def about_my_self_view(request):
    if request.method == 'GET':
        return HttpResponse('mne 23')

def my_favourite_writer_viev(request):
    if request.method == 'GET':
        return HttpResponse('Пушкин')

def facts_about_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('красиво писал, был убит как гангстер в перестрелке,' \
        ' но не факт ведь потом появился Александ Дюма, который писал таким же слогом,' \
        ' и в общем его работы были карйне схожи'
        )

def my_opinion_about_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('мое мнение таково, что это одна из самых значительных фигур в поэзии того времени')