def calulcar_velocidade_media():
    distancia = float(input("Digite a distância percorrida em KM: "))
    tempo = float(input("Digite o temmpo gasto em horas: "))

    if tempo > 0 :
        velocidade_media = distancia / tempo
        print(f"A Velocidade média é de {velocidade_media} km/h")
    else:
        print("O tempo deve ser maior que zero para calcular a velocidade média")


calulcar_velocidade_media()