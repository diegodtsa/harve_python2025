
media_consumo = int(input("Informe a média de consumo: "))

dias_consumo = int(input("Informe a quantidade de dias: "))

horas_consumo = int(input("Informe o tempo médio de horas da lampada ligada: "))

preco_kwh = float(input("Informe o consumo médio em kw/h: "))

qtd_lampadas = int(input("Informe a quantidade de Lampadas: "))

gasto_mensal = media_consumo * dias_consumo * horas_consumo * preco_kwh * qtd_lampadas

print("O gasto do nosso sistema de iluninação é de R$:",gasto_mensal)





