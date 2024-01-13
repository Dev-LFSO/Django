from django.shortcuts import render, redirect
from .models import Sala
from .forms import SalaForm
# Create your views here.

def home(request):
    salas = Sala.objects.all()
    conteudo = {'salas': salas}
    return render(request, 'base/home.html', conteudo)

def sala(request, id):
    sala = Sala.objects.get(id=id)
    conteudo = {'sala': sala}
    return render(request, 'base/sala.html', conteudo)

def criar_sala(request):
    form = SalaForm()

    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    conteudo = {'form': form}
    return render(request, 'base/sala_form.html', conteudo)

def atualizar_sala(request, id):
    sala = Sala.objects.get(id=id)
    form = SalaForm(instance=sala)

    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('home')

    conteudo = {'form': form}
    return render(request, 'base/sala_form.html', conteudo)

def apagar_sala(request, id):
    sala = Sala.objects.get(id=id)
    if request.method == 'POST':
        sala.delete()
        return redirect('home')
    conteudo = {'obj': sala}
    return render(request, 'base/deletar.html', conteudo)