#Crie uma lista que some os valores de input do usuário até que a soma ultrapasse 100. 
#Quando isso acontecer, o algoritmo deve finalizar e apresentar o total.

lista_valores = []
soma_total = 0

while soma_total <= 100:
    valor_input = int(input("Informe o valor: "))
    lista_valores.append(valor_input)
    soma_total = sum(lista_valores)
    print(f"Valores na lista: {lista_valores}")
    print(f"Soma atual: {soma_total}")

print(f"Lista de todos os valores digitados: {lista_valores}")