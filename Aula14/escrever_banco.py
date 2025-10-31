import pandas as pd
import requests
import pandas_gbq

chave = 'f8206f15'
url_tempo = f'https://api.hgbrasil.com/weather?woeid=455827&key={chave}'

response = requests.get(url_tempo)
list_forecast = response.json()['results']['forecast']
df_tempo = pd.DataFrame(data=list_forecast)
df_tempo.drop(columns=['full_date', 'humidity', 'sunrise', 'sunset', 'moon_phase'], inplace=True)
df_tempo.columns = ['data', 'dia_da_semana', 'maximo', 'minimo', 'nebulosidade', 'chuva', 'prob_chuva', 'veloc_vento', 'descricao', 'condicao']

pandas_gbq.to_gbq(df_tempo, 'python_ETL.diego_previsao_tempo', project_id= 'first-vigil-440513-q0')

