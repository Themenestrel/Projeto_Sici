from django.db.models import Model
from django.db.models import PositiveIntegerField
from django.db.models import CharField
from django.db.models import EmailField
from django.db.models import DateTimeField
from django.db.models import TextField


class Dados(Model):
    cd_ua = PositiveIntegerField(blank=True, null=True)
    sigla_ua = CharField(max_length=50, blank=True, null=True)
    nome_ua = CharField(max_length=255, blank=True, null=True)
    titular = CharField(max_length=100, blank=True, null=True)
    cargo = CharField(max_length=30, blank=True, null=True)
    cd_ua_pai = PositiveIntegerField(blank=True, null=True)  
    cd_ua_basica = PositiveIntegerField(blank=True, null=True)  
    nome_ua_basica = CharField(max_length=255, blank=True, null=True)
    sigla_ua_basica = CharField(max_length=255, blank=True, null=True)
    nat_juridica = PositiveIntegerField(blank=True, null=True)
    ordem_ua_basica = PositiveIntegerField(blank=True, null=True)
    ordem_absoluta = PositiveIntegerField(blank=True, null=True)
    ordem_relativa = PositiveIntegerField(blank=True, null=True)
    tipo_logradouro = CharField(max_length=255, blank=True, null=True)
    nome_logradouro = CharField(max_length=255, blank=True, null=True)
    trechamento_cep = CharField(db_column='trechamento_CEP', max_length=255, blank=True, null=True)
    nome_logradouro_abreviado = CharField(max_length=255, blank=True, null=True)
    nro = PositiveIntegerField(blank=True, null=True)
    complemento = CharField(max_length=255, blank=True, null=True)
    bairro = CharField(max_length=255, blank=True, null=True)
    bairro_abreviado = CharField(max_length=255, blank=True, null=True)
    localidade = CharField(max_length=255, blank=True, null=True)
    cep = CharField(max_length=255, db_column='CEP', blank=True, null=True)
    telefones = CharField(max_length=255, blank=True, null=True)
    emails = EmailField(max_length=255, blank=True, null=True)
    horario_funcionamento = CharField(max_length=255, blank=True, null=True)
    msg = TextField(max_length=255, blank=True, null=True)
    data_criacao_registro = DateTimeField(blank=True, null=True)
