import pandas as pd

df_bitcoin = pd.read_json("https://harve.com.br/praticas/binance.json")

df_bitcoin = df_bitcoin.iloc[:,:6] #Filtro do iloc primeiro ":" e o filtro de linha e o segundo ":" e o filtro de coluna, no caso buscando apenas 6 colunas.
df_bitcoin.columns = ['TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']

print(df_bitcoin.head())