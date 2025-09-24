print("Iniciando nossa calculadora!")
valor_usuario = float(input("Digite o valor que quer converter: "))
valor_conversao = input("Digite 'cm' para converter em centimentros e 'm' para converter em metros: ")

if valor_conversao == "cm":
    centimetros = valor_usuario * 100
    print(f"A medida em centimetros é: {centimetros} cm")
else:
    if valor_conversao == "m":
        metros = valor_usuario / 100
        print(f"A medida em metros é: {metros} m")
    else:
        print("Tipo de conversão inválida")
