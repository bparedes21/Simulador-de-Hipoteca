"""Reto 1
Enunciado: Dado un fichero excel con nombres y correos (columna nombre y columna email), realiza un script en Python que devuelva los mails únicos de la columna email.
Consideraciones: Utiliza la librería pandas para procesar el fichero Excel (.xls).

"""

def return_mails(Excel_df):
    mails_unique = Excel_df.email.drop_duplicates()
    return mails_unique
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas as pd

    Excel_df = pd.read_excel("DATA.xlsx")
    mails_unique=return_mails(Excel_df)
    print(mails_unique)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
