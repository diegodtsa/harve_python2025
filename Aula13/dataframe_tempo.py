import pandas as pd
import requests

chave = 'f8206f15'
url_tempo = f'https://api.hgbrasil.com/weather?woeid=455827&key={chave}'

response = requests.get(url_tempo)

df_wheather = pd.DataFrame(response.json()['results']['forecast'])
df_wheather['rain'] = round(df_wheather['rain'].astype(float),0)
df_wheather = df_wheather[['date', 'weekday', 'max', 'min', 'cloudiness', 'rain', 'rain_probability', 'wind_speedy']]
df_wheather.columns = ['DATA','DIA_SEMANA','TEMP_MAX','TEMP_MINIMO','NEBULOSIDADE','CHUVA', 'PROBABILIDADE_CHUVA', 'VELOCIDADE_VENTO']



print(df_wheather)