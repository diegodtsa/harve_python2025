while True:
    print("Calculadora Simples")
    print("Escolha a operação (+, -, *, /) ou digite 'sair' para finalizar")

    operacao = input("Qual a operação quer realizar: ").lower()

    if operacao == "sair":
        print("Saindo da Calculadora, Até Logo !")
        break

    primeiro_numero = float(input("Digite o primeiro numero: "))
    segundo_numero = float(input("Digite o segundo numero: "))

    if operacao == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao == "-":
        resultado = primeiro_numero - segundo_numero
    elif operacao == "*":
        resultado = primeiro_numero * segundo_numero
    elif operacao == "/":
        if segundo_numero != 0:
            resultado = primeiro_numero / segundo_numero
        else:
            resultado = "Erro divisão por zero! "
    else:
        resultado = "Operação Inválida. Escolha a operação (+, -, *, /) ou digite 'sair' para finalizar "
    print(f"Resultado: {resultado}")