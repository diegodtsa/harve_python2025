import pandas as pd

alturas = [1.6, 1.8, 2.0, 1.70, 2.10]

nomes = ['Roberto', 'Geovane', 'Lucas', 'Eduardo', 'Felipe']

alturas = pd.Series(alturas, index=nomes)

print(alturas.max())
print(alturas.min())
print(alturas.mean())
print(len(alturas))

#print(alturas.shape) #retorna uma tupla

#print(alturas.shape[0]) #retorna o indice da tupla

#print(alturas)

print(alturas.idxmax())

print(alturas.idxmin())
#print(alturas)

#pessoas = ['Ana', 'Roberto', 'Larissa', 'Pedro', 'Geovane']

#p = len(pessoas) -1

#print(p)