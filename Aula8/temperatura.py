import pandas as pd

temperaturas = [28, 31, 29, 33, 27, 30, 32]

s_temperaturas = pd.Series(temperaturas)

#temp_maior30 = (s_temperaturas.loc [s_temperaturas > 30]) #Outra forma de fazer

temp_maior30 = (s_temperaturas > 30).sum() #Outra forma de fazer com .sum()

#print(f"A Quantidade de dias acima dos 30 graus foi {len(temp_maior30)} dias")

print(f"A Quantidade de dias acima dos 30 graus foi {temp_maior30} dias")