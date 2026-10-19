from django.shortcuts import render, get_object_or_404, redirect
from .models import Anketa
from .forms import AnketaForm

# 1. READ: Список всех анкет
def anketa_list_view(request):
    anketas = Anketa.objects.all().order_by('-created_at')
    return render(request, 'anketa/anketa_list.html', {'anketas': anketas})

def anketa_detail_view(request, id):
    anketa = get_object_or_404(Anketa, id=id)
    return render(request, 'anketa/anketa_detail.html', {'anketa': anketa})

def anketa_create_view(request):
    if request.method == 'POST':
        form = AnketaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('anketa_list')
    else:
        form = AnketaForm()
    return render(request, 'anketa/anketa_create.html', {'form': form})

def anketa_update_view(request, id):
    anketa = get_object_or_404(Anketa, id=id)
    if request.method == 'POST':
        form = AnketaForm(request.POST, request.FILES, instance=anketa)
        if form.is_valid():
            form.save()
            return redirect('anketa_detail', id=anketa.id)
    else:
        form = AnketaForm(instance=anketa)
    return render(request, 'anketa/anketa_update.html', {'form': form, 'anketa': anketa})

def anketa_delete_view(request, id):
    anketa = get_object_or_404(Anketa, id=id)
    if request.method == 'POST':
        anketa.delete()
        return redirect('anketa_list')
    return render(request, 'anketa/anketa_delete_confirm.html', {'anketa': anketa})