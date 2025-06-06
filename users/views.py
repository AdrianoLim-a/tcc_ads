from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from .models import Endereco
from django.http import HttpResponse
from django.contrib import messages

def logout_view(request):
    return logout_then_login(request)

def cadastro(request):
    user = User()

    if request.method == 'POST':
        if request.POST.get('password') != request.POST.get('confirm-password'):
            messages.error(request, "As senhas não coincidem!")
            return redirect('cadastro')
        user.cpf = request.POST.get('cpf')
        user.first_name = request.POST.get('nome')
        user.username = request.POST.get('nome')
        user.email = request.POST.get('email')
        user.last_name = request.POST.get('sobrenome')
        user.telefone = request.POST.get('telefone')
        senha = request.POST.get('password')
        user.type_user = request.POST.get('type')
        if senha:
            user.set_password(senha)
        user.save()
        messages.success(request, "Cadastro realizado com sucesso!")
    return render(request, 'cadastro.html')



@login_required
def ticketUsuario(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'cliente/ticketUsuario.html')

def ticketPrestador(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'prestador/ticketPrestador.html')

def detalhesPedido(request):
    #if request.user.type_user == 'P':
        #TODO refactor
        #return HttpResponse('*Fazer uma paǵina 404*')
    return render(request, 'cliente/detalhesPedido.html')



