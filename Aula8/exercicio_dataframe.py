import pandas as pd

df = pd.DataFrame({
    "Aluno": ["Ana", "Bruno", "Carla", "Diego", "Elisa"],
    "Prova_1": [7, 5, 9, 6, 8],
    "Prova_2": [6, 7, 8, 5, 9]
})

df["Média"] = (df["Prova_1"] + df["Prova_2"]) / 2

aluno_aprovado = df.loc[df["Média"] >= 7, ["Aluno","Média"]]



#print(df)

print(aluno_aprovado)