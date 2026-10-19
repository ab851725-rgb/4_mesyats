from django.views.generic import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('это второй')

class MyFavouriteEmojiView(View):
    def get(self, request):
        return HttpResponse('🟢🟤🔵⚪⚫🟠')

class AboutMySelfView(View):
    def get(self, request):
        return HttpResponse('mne 23')

class MyFavouriteWriterView(View):
    def get(self, request):
        return HttpResponse('Пушкин')

class FactsAboutWriterView(View):
    def get(self, request):
        return HttpResponse('красиво писал, был убит как гангстер в перестрелке, но не факт ведь потом появился Александ Дюма, который писал таким же слогом, и в общем его работы были карйне схожи')

class MyOpinionWriterView(View):
    def get(self, request):
        return HttpResponse('мое мнение таково, что это одна из самых значительных фигур в поэзии того времени')