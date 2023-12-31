import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

fecha_list = []
pib_eur_list = []
pib_dol_list = []
variacion_list = []

url = 'https://datosmacro.expansion.com/pib/ecuador'

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')

tabla = soup.find('table', attrs={'class': 'table tabledat table-striped table-condensed table-hover'})

filas = tabla.find_all('tr')
for fila in filas:
    celdas = fila.find_all_next('td')
    if len(celdas) > 0:
        fecha = celdas[0].string
        pib_eur = re.sub(r'[^\d.]', '', str(celdas[1].string))
        pib_dol = re.sub(r'[^\d.]', '', str(celdas[2].string))
        variacion = celdas[3].string
        fecha_list.append(fecha)
        pib_eur_list.append(pib_eur)
        pib_dol_list.append(pib_dol)
        variacion_list.append(variacion)

df = pd.DataFrame({'FECHA': fecha_list,'PIB (EUROS)': pib_eur_list,'PIB (DOLARES)': pib_dol_list, 'VARIACION PIB':variacion_list})
df.to_csv('pibEcuador.csv', index=False, encoding='utf-8')












# for table in soup.findAll('table', attrs={'class': 'table tabledat table-striped table-condensed table-hover'}):
#     print(table)
#     fecha = table.find('td', attrs={'class':'fecha'})
#     print(fecha)
#     pib = table.find('td', attrs={'class':'numero eur'})
#     print(pib)
#     var = table.find('td', attrs={'class':'numero'})
#     print(var)
#
#     fechas.append(fecha.text)
#     pibs.append(pib.text)
#     vars.append(var.text)



    # if fecha is not None:
    #     fechas.append(fecha.text.strip())

# df = pd.DataFrame({'FECHA': fechas,'PIB': pib,'Var.PIB': var})
# df.to_csv('prueba3.csv', index=False, encoding='utf-8')





























# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
#
# fechas = []
# pib = []
# var = []
#
# url = 'https://datosmacro.expansion.com/pib/ecuador'
#
# html_doc = requests.get(url)
# soup = BeautifulSoup(html_doc.text, 'html.parser')
#
# for table in soup.find_all('table', attrs={'class': 'table tabledat table-striped table-condensed table-hover'}):
#     for row in table.find_all('tr'):
#         columns = row.find_all('td')
#         if len(columns) >= 3:
#             fecha = columns[0].text.strip()
#             pib_value = columns[1].text.strip()
#             var_value = columns[2].text.strip()
#             fechas.append(fecha)
#             pib.append(pib_value)
#             var.append(var_value)
#
# df = pd.DataFrame({'FECHA': fechas, 'PIB': pib, 'Var.PIB': var})
# df.to_csv('prueba2.csv', index=False, encoding='utf-8')
