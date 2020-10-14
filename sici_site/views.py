from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pyodbc
from django.conf import settings
from sici_site.models import Dados

# Create your views here.

def home(request):
    dados_totais = Dados.objects.all()

    busca_cd_ua = request.GET.get('cd_ua')
    busca_nome_ua_basica = request.GET.get('nome_ua_basica')
    busca_titular = request.GET.get('titular')

    if busca_cd_ua:
        dados_totais = Dados.objects.filter(cd_ua=busca_cd_ua).order_by('data_criacao_registro').last()
    elif busca_nome_ua_basica:
        dados_totais = Dados.objects.filter(nome_ua_basica__icontains=busca_nome_ua_basica).order_by(
            'data_criacao_registro').last()
    elif busca_titular:
        dados_totais = Dados.objects.filter(titular__icontains=busca_titular).order_by('data_criacao_registro').last()

    return render(request, 'sici_site/home.html', {'dados_totais': dados_totais})
