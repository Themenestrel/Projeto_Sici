from django.shortcuts import render
from sici_site.models import Dados


def home(request):
    tipo_consulta = request.GET.get("consulta", None)
    busca = request.GET.get("busca")
    dados = None

    if tipo_consulta == "cd_ua":
        try:
            dados = Dados.objects.filter(cd_ua=int(busca)).order_by('data_criacao_registro').last()
        except ValueError:
            pass
    elif tipo_consulta == "nome":
        dados = Dados.objects.filter(nome_ua__icontains=busca).order_by('titular')
    elif tipo_consulta == "gestor":
        dados = Dados.objects.filter(titular__icontains=busca).order_by('titular')
    return render(request, 'sici_site/home.html', {'dados': dados, 'tipo': tipo_consulta})
