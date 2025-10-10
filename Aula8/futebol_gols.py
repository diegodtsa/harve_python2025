import pandas as pd

gols_pro = [2, 3, 1, 0, 1, 2, 4]
gols_contra = [1, 0, 2, 1, 1, 2, 2]
#Rodada = ['Rodada 1', 'Rodada 2', 'Rodada 3', 'Rodada 4', 'Rodada 5', 'Rodada 6', 'Rodada 7']

#list comprehension
rodadas = [f"Rodada {i}" for i in range(1, 8)]


s_gols_pro = pd.Series(gols_pro, index = rodadas)
s_gols_contra = pd.Series(gols_contra, index = rodadas)

saldo_gols = s_gols_pro - s_gols_contra

#print(s_gols_pro)

#print(s_gols_contra)

print(saldo_gols)

print(f"A Rodada em que o time marcou mais gols foi a {s_gols_pro.idxmax()} ")
print(f"O Saldo até a rodada 7 é {saldo_gols.sum()} gols")

print(s_gols_pro.mean())
