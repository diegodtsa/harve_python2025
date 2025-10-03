while True:

    if valor_c== "sair":
        break
    else:
        valor_a = int(input("Informe o primeiro valor: "))

        simbol = input("Informe a operação: +, -, /, * ")

        valor_b = int(input("Informe o segundo valor: "))

        if simbol == "+":
            operacao = valor_a + valor_b
        if simbol == "-":
            operacao = valor_a - valor_b
        if simbol == "*":
            operacao = valor_a * valor_b
        if simbol == "/":
            operacao = valor_a / valor_b
        
print(f"O valor da operação é {operacao}")
