import pandas as pd

df_dados = pd.read_csv("http://www.harve.com.br/praticas/dados_etl.csv", sep='\t')

df_dados["Idade"] = 2025 - df_dados["Year_Birth"]

df_dados["Total de Filhos"] = df_dados["Kidhome"] + df_dados["Teenhome"]

#print(df_dados[["Kidhome","Teenhome","Total de Filhos"]].head())

#print(df_dados[["Year_Birth","Idade"]].head())

#print(df_dados.head())


df_dados["Total de Vendas"] = df_dados["NumDealsPurchases"] + df_dados["NumWebPurchases"] + df_dados["NumCatalogPurchases"]+ df_dados["NumStorePurchases"]

def definirclasse(valor):
    if valor < 20000:
        return "Baixo"
    if valor < 40000:
        return "Médio"
    if valor < 60000:
        return "Alto"
    return "Muito Alto"
    
df_dados["Categoria_gasto"] = df_dados["Income"].apply(lambda x : definirclasse(x))

print(df_dados[["Income","Categoria_gasto"]].head())

#print(df_dados.info())