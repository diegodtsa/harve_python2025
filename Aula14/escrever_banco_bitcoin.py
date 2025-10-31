import pandas as pd
import pandas_gbq
import requests

df_bitcoin = pd.read_json('https://harve.com.br/praticas/binance.json')
df_bitcoin.drop(columns=[6, 7, 8, 9, 10, 11], inplace=True)
df_bitcoin.columns = ['TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']

pandas_gbq.to_gbq(df_bitcoin, 'python_ETL.diego_bitcoin', project_id= 'first-vigil-440513-q0')

