from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from sici_site.models import Dados

# Create your views here.

def home(request):

    dados_totais = None
    dados_nome_ua = None
    dados_titular = None

    busca_cd_ua = request.POST.get('cd_ua')
    busca_nome_ua = request.POST.get('nome_ua')
    busca_titular = request.POST.get('titular')

    if busca_cd_ua:
        dados_totais = Dados.objects.filter(cd_ua=busca_cd_ua).order_by('data_criacao_registro').last()
    elif busca_nome_ua:
        dados_nome_ua = Dados.objects.filter(nome_ua__contains=busca_nome_ua).order_by()
    elif busca_titular:
        dados_titular = Dados.objects.filter(titular__contains=busca_titular).order_by()

    return render(request, 'sici_site/home.html', {'dados_totais': dados_totais, 'dados_nome_ua': dados_nome_ua, 'dados_titular': dados_titular})

