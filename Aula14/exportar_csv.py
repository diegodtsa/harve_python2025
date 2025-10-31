import pandas as pd

df_bitcoin = pd.read_json('https://harve.com.br/praticas/binance.json')
df_bitcoin.drop(columns=[6, 7, 8, 9, 10, 11], inplace=True)
df_bitcoin.columns = ['TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']

df_bitcoin.to_csv('bitcoin_2.csv', index=False, sep=';')