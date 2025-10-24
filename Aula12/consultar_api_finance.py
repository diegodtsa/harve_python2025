import pandas as pd
import requests as r


chave_fin = '3b9b39d6'
url_fin = 'https://api.hgbrasil.com/'
rota_fin = 'finance?'

url_completa_fin = f'{url_fin}{rota_fin}key={chave_fin}'

response = r.get(url_completa_fin)
dolar_hoje = response.json()['results']['currencies']['USD']['buy']



valor_real = float(input("Informe o valor do Real: "))

conversao = valor_real / dolar_hoje

print(f"O valor de R$ {valor_real:.2f} valem USD {conversao:.2f}")
print(f"Cotação do dolar hoje é {dolar_hoje}")



