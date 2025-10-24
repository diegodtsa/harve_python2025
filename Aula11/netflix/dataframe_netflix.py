import pandas as pd

df_netflix = pd.read_csv("http://www.harve.com.br/praticas/NetflixViewingHistory.csv")

def categoria(titulo):
    if ":" in titulo:
        return "Série"
    else:
        return "Filme"
    

df_netflix["Categoria"] = df_netflix["Title"].apply(lambda x : categoria(x))

print(df_netflix[["Title", "Categoria"]].head(10))

#print(df_netflix.info())

print(df_netflix["Categoria"].value_counts())

