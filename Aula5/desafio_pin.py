#Vamos fazer o programa que faria você ficar rico no programa Silvio Santos. 
# Um algoritmo que solucione sempre o jogo do pin. Para entender o jogo, iremos inserir um múltiplo e o limite e dentro desses parâmetros, 
# faremos o programa imprimir a contagem de acordo com o pin. Nela, devemos contar 1,2,3... até o limite. 
# Porém, quando chegar no número múltiplo, devemos dizer pin ao invés do número e continuar a contagem. 
# Quando chegar novamente no múltiplo, o raciocínio se repete.

multiplo = int(input("Digite o numero multiplo para o Pin: "))

limite = int(input("Digite o Limite para finalizar o jogo: "))

contador = 1

while contador <= limite:
    if contador % multiplo == 0:
        print("pin")
    else:
        print(contador)
    contador += 1    