import pandas as pd

temp_max_semana = pd.Series([38, 39, 37, 30, 32, 25, 29], index = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo'])
temp_min_semana = pd.Series([25, 29, 27, 20, 22, 15, 19], index = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo'])

print(temp_min_semana.min())
print(temp_max_semana.max())

amplitude = temp_max_semana - temp_min_semana

#amplitude_dia = pd.Series(temp_max_semana - temp_min_semana).max()


print(amplitude)
