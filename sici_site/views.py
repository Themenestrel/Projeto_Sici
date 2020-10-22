from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from sici_site.models import Dados

# Create your views here.

def home(request):
    tipo_consulta = request.GET.get("consulta")
    busca = request.GET.get("busca")
    dados = None

    if tipo_consulta == "cd_ua":
        dados = Dados.objects.filter(cd_ua=int(busca)).order_by('data_criacao_registro').last()
    elif tipo_consulta == "nome":
        dados = Dados.objects.filter(nome_ua__contains=busca).order_by('cd_ua')
    elif tipo_consulta == "titular":
        dados = Dados.objects.filter(titular__contains=busca).order_by('cd_ua')
    return render(request, 'sici_site/home.html', {'dados': dados, 'tipo':tipo_consulta})
