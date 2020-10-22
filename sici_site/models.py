# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dados(models.Model):
    cd_ua = models.IntegerField(blank=True, null=True)
    sigla_ua = models.TextField(blank=True, null=True)  # This field type is a guess.
    nome_ua = models.TextField(blank=True, null=True)  # This field type is a guess.
    titular = models.TextField(blank=True, null=True)  # This field type is a guess.
    cargo = models.TextField(blank=True, null=True)  # This field type is a guess.
    cd_ua_pai = models.TextField(blank=True, null=True)  # This field type is a guess.
    cd_ua_basica = models.TextField(blank=True, null=True)  # This field type is a guess.
    nome_ua_basica = models.TextField(blank=True, null=True)  # This field type is a guess.
    sigla_ua_basica = models.TextField(blank=True, null=True)  # This field type is a guess.
    nat_juridica = models.TextField(blank=True, null=True)  # This field type is a guess.
    ordem_ua_basica = models.TextField(blank=True, null=True)  # This field type is a guess.
    ordem_absoluta = models.TextField(blank=True, null=True)  # This field type is a guess.
    ordem_relativa = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo_logradouro = models.TextField(blank=True, null=True)  # This field type is a guess.
    nome_logradouro = models.TextField(blank=True, null=True)  # This field type is a guess.
    trechamento_cep = models.TextField(db_column='trechamento_CEP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nome_logradouro_abreviado = models.TextField(blank=True, null=True)  # This field type is a guess.
    nro = models.TextField(blank=True, null=True)  # This field type is a guess.
    complemento = models.TextField(blank=True, null=True)  # This field type is a guess.
    bairro = models.TextField(blank=True, null=True)  # This field type is a guess.
    bairro_abreviado = models.TextField(blank=True, null=True)  # This field type is a guess.
    localidade = models.TextField(blank=True, null=True)  # This field type is a guess.
    cep = models.TextField(db_column='CEP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    telefones = models.TextField(blank=True, null=True)  # This field type is a guess.
    emails = models.TextField(blank=True, null=True)  # This field type is a guess.
    horario_funcionamento = models.TextField(blank=True, null=True)  # This field type is a guess.
    msg = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_criacao_registro = models.DateTimeField(blank=True, null=True)