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

    class Meta:
        managed = False
        db_table = 'Dados'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
