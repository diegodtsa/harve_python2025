import pandas as pd

df = pd.read_csv("dataset-worldpop.csv")

#Encontre a população registrada para o Brasil no ano mais recente disponível. (Note que o nome dos países está em inglês, então procure por Brazil)
#df = df.loc[df["Country/Territory"] == "Brazil"]

#Qual o país mais populoso da Europa no ano de 2022?
filtro_europa = df.loc[df["Continent"] == "Europe", ["Country/Territory","2022 Population"]]
mais_populoso_europa = filtro_europa['2022 Population'].max()

x= filtro_europa.loc[ filtro_europa['2022 Population'] == mais_populoso_europa]

#Liste os países da África e suas populações para o ano de 2020.
filtro_africa = df.loc[df["Continent"] == "Africa", ["Country/Territory","2020 Population"]]


#Mostre como a população da Índia variou ao longo dos anos disponíveis. (selecione as colunas das populações ao longo dos anos filtrando apenas o país India)
india = df.loc[df["Country/Territory"] == "India", 
              ["Country/Territory",
               "2022 Population", 
               "2020 Population", 
               "2015 Population",
               "2010 Population",
               "2000 Population",
               "1990 Population",
               "1980 Population",
               "1970 Population"]]


#mais_populoso = df.loc[df["2022 Population"]]

#maior_populacao = mais_populoso.max()

#print(mais_populoso)

#print(india)

#print(maior_populacao)

#print(filtro_europa)
print(x)

#print(filtro_africa)

#print(df.describe())