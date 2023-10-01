import pandas as pd
import openpyxl
import os
import ctypes  # An included library with Python install.
from urllib.parse import quote_plus
from sqlalchemy import create_engine
import pymysql


dados = [
    ['TB_STG_MAPA_SPOOLS', 'Mapa Spools.xlsx'],
    ['TB_STG_MAPA_SUPORTE', 'Mapa Suportes.xlsx'],
    ['TB_STG_MAPA_JUNTAS', 'Mapa Juntas.xlsx']
]
dados1 = [
    ['TB_STG_MAPA_SPOOLS', 'Mapa Spools.xlsx']
]



def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def extrair_arquivos(tabela, arquivo):
    engine = create_engine("mysql+pymysql://zep_palmont:%s@186.202.152.83:3306/zep_palmont" % quote_plus("Pm143625@"))
    df = pd.read_sql(f"select * from {tabela}", engine)
    df.to_excel(f'arquivos/{arquivo}', sheet_name=arquivo.split('.xlsx')[0], index=False)
    return df


if __name__ == '__main__':
    Mbox('Extração dos arquivos', 'Será iniciada a extração', 1)
    if not os.path.isdir('arquivos'):
        os.mkdir('arquivos')

    for mapa in dados:
        arquivo = extrair_arquivos(mapa[0], mapa[1])
        # arquivo.to_excel(f'arquivos/{mapa[1]}', index=False)

    Mbox('Extração dos arquivos', 'Extração concluída com exito', 1)




