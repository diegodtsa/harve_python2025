import pandas as pd

df_bitcoin = pd.read_json('https://harve.com.br/praticas/binance.json', dtype=str)
df_bitcoin.drop(columns=[6, 7, 8, 9, 10, 11], inplace=True)
df_bitcoin.columns = ['TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']

print(df_bitcoin.head())

df_bitcoin[['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']] = round(df_bitcoin[['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']].astype(float), 2)


print(df_bitcoin.head())