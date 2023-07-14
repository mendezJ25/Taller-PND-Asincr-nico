import pandas as pd
import requests
from bs4 import BeautifulSoup

fechas = []
pibs = []
vars = []

url = 'https://datosmacro.expansion.com/pib/ecuador'

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')

for table in soup.findAll('table', attrs={'class': 'table tabledat table-striped table-condensed table-hover'}):
    print(table)
    fecha = table.find('td', attrs={'class':'fecha'})
    print(fecha)
    pib = table.find('td', attrs={'class':'numero eur'})
    print(pib)
    var = table.find('td', attrs={'class':'numero'})
    print(var)

    fechas.append(fecha.text)
    pibs.append(pib.text)
    vars.append(var.text)



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
