import pandas as pd

df_titanic = pd.read_csv("titanic-pt-BR.csv")


#print(df_titanic.head())

def categoria_idade(idade):
    if idade < 10:
        return "Criança"
    if idade < 20:
        return "Jovem"
    if idade < 60:
        return "Adulto"
    if idade >= 60:
        return "Idoso"
    
df_titanic["Categoria"] = df_titanic["Idade"].apply(lambda x : categoria_idade(x))

print(df_titanic["Categoria"].value_counts())

#print(df_titanic.info())


#print(df_titanic[["Idade", "Categoria"]])