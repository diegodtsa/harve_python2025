import pandas as pd

df = pd.DataFrame({
    "Aluno": ["Ana", "Bruno", "Carla", "Diego", "Elisa"],
    "Prova_1": [7, 5, 9, 6, 8],
    "Prova_2": [6, 7, 8, 5, 9]
})

df["Média"] = (df["Prova_1"] + df["Prova_2"]) / 2

df["Aumento de Desempenho"] = (df["Prova_2"] - df["Prova_1"] )

aumento_desempenho = df.loc[df["Aumento de Desempenho"]> 1]

#df["Aumento de Desempenho"] = df.loc[df["Prova_2"] >= df["Prova_1"]]

#aluno_aprovado = df.loc[df["Média"] >= 7, ["Aluno","Média"]]

print(aumento_desempenho)


#print(aluno_aprovado)