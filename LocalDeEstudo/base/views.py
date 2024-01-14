from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Sala, Topico
from .forms import SalaForm
# Create your views here.

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuário não encontrado!')

        user = authenticate(request, username=username, password=senha)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha não foram encontrados!')

    conteudo = {}
    return render(request, 'base/login.html', conteudo)

def deslogar(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    salas = Sala.objects.filter(Q(topico__nome__icontains=q) | 
                                Q(nome__icontains=q) |
                                Q(descricao__icontains=q))
    topicos = Topico.objects.all()
    qntd_salas = salas.count() 
    conteudo = {'salas': salas, 'topicos': topicos, 'qntd_salas': qntd_salas}
    return render(request, 'base/home.html', conteudo)

def sala(request, id):
    sala = Sala.objects.get(id=id)
    conteudo = {'sala': sala}
    return render(request, 'base/sala.html', conteudo)

@login_required(login_required='/login')
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