from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pyodbc
from django.conf import settings
from sici_site.models import Dados

# Create your views here.

def home(request):
    dado = Dados.objects.get(cd_ua='1800')
    return render(request, 'sici_site/home.html', {'dado': dado})
