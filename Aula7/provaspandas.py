import pandas as pd

prova_1 = [5, 7, 8]
prova_2 = [10, 7, 3]
nomes = ["Ana", "Beto", "Carlos"]

prova_1 = pd.Series(prova_1, index = nomes)
prova_2 = pd.Series(prova_2, index = nomes)

print((prova_1 + prova_2) / 2)