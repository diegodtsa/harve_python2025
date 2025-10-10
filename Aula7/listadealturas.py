import pandas as pd

altura_jogadores = [1.90, 1.98, 1.95, 2.05, 2.10]

nome_jogadores = ["Roberto", "Pedro", "Ricardo,", "Rodrigo", "Ronaldo"]

x = pd.Series(altura_jogadores)

y = pd.Series(altura_jogadores, index=nome_jogadores)

print(x.max())

print(x.min())

print(x.mean())

print(y.index)

