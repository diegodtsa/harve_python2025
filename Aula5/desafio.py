#Crie uma lista que some os valores de input do usuário até que seja digitado 0. 
# Quando o 0 for digitado, o algoritmo deve finalizar e apresentar o total.

lista = []

while True:
    valor = (input("Digite um valor para realizar a soma ou 'sair' para finalizar:")).lower()
    if valor == "sair" :
        break
    else:
        lista.append(int(valor))

total_lista = sum(lista)

print(f"O total dos valores digitados é: {total_lista} ")