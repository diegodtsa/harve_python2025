import pandas as pd
import requests as r


chave_fin = ''
url_fin = ''
rota_fin = 'finance?'

url_completa_fin = f'{url_fin}{rota_fin}key={chave_fin}'

response = r.get(url=url_completa_fin)

print(f'{url_fin}{rota_fin}key={chave_fin}')

print(response)

