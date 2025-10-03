def jogo_pin():
    multiplo = int(input("Digite o número multiplo para o pin: "))
    limite = int(input("Digite o limite do jogo: "))

    contador = 1

    while contador <= limite:
        if contador % multiplo == 0:
            print("Pin")
        else:
            print(contador)
        contador += 1

jogo_pin()        
