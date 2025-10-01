lista_valores = [11, 22, 51, 86, 12, 71, 63,]

somatorio_total = 0
contagem = 0

for item in lista_valores:
    somatorio_total = somatorio_total + item
    contagem = contagem + 1 #podendo ser também -> contagem += 1
    print(contagem, somatorio_total)
 

media = round(somatorio_total / contagem)


print(f"A media aritmetica é: {media}")