import pandas as pd

df= pd.DataFrame()

dados = [
    {"Cliente": "Ana",      "Data_Nascimento": "28/04/1997", "Idade": 28, "Cidade": "São Paulo", "Compras": 5},
    {"Cliente": "Bruno",    "Data_Nascimento": "12/10/1980", "Cidade": "Rio de Janeiro", "Compras": 2},
    {"Cliente": "Carla",    "Data_Nascimento": "01/09/1990", "Idade": 35,},
    {"Cliente": "Diego",    "Data_Nascimento": "02/10/1985", "Idade": 40, "Cidade": "Belo Horizonte", "Compras": 8},
    {"Cliente": "Elisa",    "Data_Nascimento": "10/01/1964", "Cidade": "Curitiba", "Compras": 10},
    {"Cliente": "Fernando", "Data_Nascimento": "10/12/2002", "Idade": 22, "Compras": 1},
    {"Cliente": "Gabriela", "Data_Nascimento": "03/06/1995", "Idade": 30, "Cidade": "Porto Alegre", },
    {"Cliente": "Hugo",     "Data_Nascimento": "14/08/1986", "Cidade": "São Paulo", "Compras": 3},
    {"Cliente": "Isabela",  "Data_Nascimento": "02/02/1988", "Idade": 37, "Compras": 4},
    {"Cliente": "João",     "Data_Nascimento": "01/03/1992", "Idade": 33, "Cidade": "Salvador"}
]

df["Clientes"] = dados

print(df.info())

