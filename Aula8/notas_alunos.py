import pandas as pd

notas = [5.5, 8.0, 7.2, 4.9, 6.3]
alunos = ['Ana', 'Beto', 'Claudio', 'Daniel', 'Eduardo']

s_notas = pd.Series(notas, index= alunos)



print(s_notas)