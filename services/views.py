from django.shortcuts import render
from .models import TicketServico
from users.models import Endereco


def cadastroTicket(request):
    ticket = TicketServico()
    endereco = Endereco()
    if request.method == 'POST':
        
        endereco.cep = request.POST.get('cep')
        endereco.logradouro = request.POST.get('logradouro')
        endereco.numero = request.POST.get('numero')
        endereco.complemento = request.POST.get('complemento')
        endereco.bairro = request.POST.get('bairro')
        endereco.cidade = request.POST.get('cidade')
        endereco.estado = request.POST.get('estado')
        #TODO: automatizar
        endereco.referencia = "NA"
        endereco.pais = "BRASIL"
        endereco.tipo = "NA"
        endereco.save()

        ticket.status = "A"
        ticket.solicitante = request.user
        ticket.categoria = request.POST.get('categoria')
        ticket.descricao = request.POST.get('descricao')
        ticket.endereco = endereco
        ticket.imagem = request.FILES.get('imagem')
        ticket.save()
    return render(request, 'cliente/ticket.html')






