import pandas as pd

df = pd.DataFrame({
    "nome": ["Marlon", "Nícolas", "Osvaldo", "Paulo", "Roberto"],
    "altura": [160, 175, 168, 180, 155],
    "peso": [55, 70, 80, 85, 60]
})

#buscando o mais alto
altura_max = df["altura"].max()
mais_alto = df.loc[df["altura"] == altura_max, ["nome","altura"]]


#buscando o mais baixo
altura_min = df["altura"].min()
mais_baixo = df.loc[df["altura"] == altura_min, ["nome","altura"]]

#buscando o mais pesado
peso_max = df["peso"].max()
mais_pesado = df.loc[df["peso"] == peso_max, ["nome","peso"]]

#buscando o mais leve
peso_min = df["peso"].min()
menos_pesado = df.loc[df["peso"] == peso_min, ["nome", "peso"]]


#print(mais_alto)

#print(mais_baixo)

print(mais_pesado)

print(menos_pesado)