import sqlite3
from datetime import datetime

from sici_site.models import Dados


def migrar():
    while True:
        continuar = input('Aperte S para continuar ou N para cancelar: ').lower()
        if continuar == 's':
            break
        elif continuar == 'n':
            return
        else:
            pass
    while True:
        try:
            banco = input('Digite o endereço completo do banco de dados ou o nome dele \ncaso esteja na raiz do '
                          'projeto (não esqueça de colocar a extensão): ')
            dados = sqlite3.connect(banco)
            c = dados.cursor()
            c.execute("select * from Dados")
            todos_dados = list(c)
            c.close()
            break
        except sqlite3.OperationalError:
            print('ERRO! Banco de dados inexistente')

    for dado in todos_dados:
        print(dado)
        inserir = Dados(
            cd_ua=dado[1] if dado[1] != 'None' else None,
            sigla_ua=dado[2] if dado[2] != 'None' else None,
            nome_ua=dado[3] if dado[3] != 'None' else None,
            titular=dado[4] if dado[4] != 'None' else None,
            cargo=dado[5] if dado[5] != 'None' else None,
            cd_ua_pai=dado[6] if dado[6] != 'None' else None,
            cd_ua_basica=dado[7] if dado[7] != 'None' else None,
            nome_ua_basica=dado[8] if dado[8] != 'None' else None,
            sigla_ua_basica=dado[9] if dado[9] != 'None' else None,
            nat_juridica=dado[10] if dado[10] != 'None' else None,
            ordem_ua_basica=dado[11] if dado[11] != 'None' else None,
            ordem_absoluta=dado[12] if dado[12] != 'None' else None,
            ordem_relativa=dado[13] if dado[13] != 'None' else None,
            tipo_logradouro=dado[14] if dado[14] != 'None' else None,
            nome_logradouro=dado[15] if dado[15] != 'None' else None,
            trechamento_cep=dado[16] if dado[16] != 'None' else None,
            nome_logradouro_abreviado=dado[17] if dado[17] != 'None' else None,
            nro=dado[18] if dado[18] != 'None' else None,
            complemento=dado[19] if dado[19] != 'None' else None,
            bairro=dado[20] if dado[20] != 'None' else None,
            bairro_abreviado=dado[21] if dado[21] != 'None' else None,
            localidade=dado[22] if dado[22] != 'None' else None,
            cep=dado[23] if dado[23] != 'None' else None,
            telefones=dado[24] if dado[24] != 'None' else None,
            emails=dado[25] if dado[25] != 'None' else None,
            horario_funcionamento=dado[26] if dado[26] != 'None' else None,
            msg=dado[27] if dado[27] != 'None' else None,
            data_criacao_registro=datetime.strptime(dado[28] + ' UTC-0300', '%Y-%m-%d %H:%M:%S.%f %Z%z') if
            dado[28] != 'None' else None
        )
        inserir.save()


if __name__ == '__main__':
    migrar()
