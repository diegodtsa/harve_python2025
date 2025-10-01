lista_valores = [11, 22, 51, 86, 12, 71, 63,]

somatorio_total = 0

for item in lista_valores:
    somatorio_total = somatorio_total + item
 

media = round(somatorio_total / len(lista_valores))


print(f"A media aritmetica é: {media}")