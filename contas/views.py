from django.shortcuts import render, redirect
from .models import *
from .form import *

def sobre(request):
  return render(request, 'contas/sobre.html')

def listagem(request):
  data = {}
  transacoes = Transacao.objects.all().order_by('dt_creation')
  data['transacoes'] = transacoes
  saldo = 0
  entrada = "Entrada de Dinheiro"
  for transacao in transacoes:
    if transacao.category.name == entrada:
      saldo = saldo + transacao.value
    else:
      saldo = saldo - transacao.value

  data['saldo'] = saldo


  return render(request, 'contas/listagem.html', data)

def criar(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect("listagem")

    data = {}
    data['form'] = form
    return render(request, 'contas/criar.html', data)

def atualizar(request, pk):
  transacao = Transacao.objects.get(pk=pk)
  form = TransacaoForm(request.POST or None, instance=transacao)
  if form.is_valid():
      form.save()
      return redirect("listagem")

  data = {}
  data['transacao'] = transacao
  data['form'] = form
  return render(request, 'contas/atualizar.html', data)

def excluir(request, pk):
  transacao = Transacao.objects.get(pk=pk)
  transacao.delete()
  return redirect('listagem')
