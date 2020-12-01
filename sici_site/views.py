from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils.timezone import make_aware

from sici_site.models import Dados


def home(request):
    if request.method == 'GET':
        tipo_consulta = request.GET.get("consulta", None)
        busca = request.GET.get("busca")
        dados = None

        if tipo_consulta == "cd_ua":
            dados = Dados.objects.filter(cd_ua=busca).order_by('-data_criacao_registro').values('cd_ua',
                                                                                                'nome_ua',
                                                                                                'titular')
        elif tipo_consulta == "nome":
            dados = Dados.objects.filter(nome_ua__icontains=busca).order_by('nome_ua').values('cd_ua',
                                                                                              'nome_ua',
                                                                                              'titular')
        elif tipo_consulta == "titular":
            dados = Dados.objects.filter(titular__icontains=busca).order_by('titular').values('cd_ua',
                                                                                              'nome_ua',
                                                                                              'titular')

        return render(request, 'sici_site/home.html', {'dados': dados, 'tipo': tipo_consulta})


def unidade(request, **kwargs):
    if request.method == 'GET':
        if 'data' in request.GET:
            data = request.GET['data'].split('-')
            data_busca = make_aware(datetime(int(data[0]), int(data[1]), int(data[2])) + timedelta(1))
        else:
            hoje = datetime.now()
            data_busca = make_aware(datetime(hoje.year, hoje.month, hoje.day) + timedelta(1))

        busca = kwargs['cod_ua']
        dados = Dados.objects.filter(cd_ua=busca, data_criacao_registro__lt=data_busca).last()
        return render(request, 'sici_site/unidade.html', {'dados': dados})
