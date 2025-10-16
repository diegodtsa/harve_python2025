import pandas as pd


df = pd.read_csv("dataset-netflix.csv")


filmes = df.loc[df["type"] == "Movie"]

#filmes_antigos = df.loc[df["release_year"] < 2000]

filmes_antigos = filmes[filmes["release_year"] < 2000]

filmes_spielberg = filmes_antigos[filmes_antigos["director"] == "Steven Spielberg"]



display(filmes_spielberg)
#print(filmes_antigos.head())
#print(filmes.head())
