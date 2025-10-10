import pandas as pd

df = pd.DataFrame() #Inicializa um dataframe vázio
ano_atual = 2025

df["Nome"] = ["Andre", "Bianca", "Carlos", "Daniel"]
df["Idade"] = [20, 25, 30, 50]
df["Nota"] = [7.5, 9.8, 10.0, 5.5]
df["Ano Nascimento"] = ano_atual - df["Idade"]


#df['Nome'] = ['Andre','Bia','Carlos','Daniel']

#print(df.head(2)) #Mostra cabeça as 2 primeiras linhas
#print(df.tail(2)) #Mostra rabo as 2 ultimas linhas

#print(df.drop("Nota", axis="columns")) #Elimina a coluna Nota

print(df)