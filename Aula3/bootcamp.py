''' distancia_km = float(input("Informe a distância em Km: "))

consumo_medio = float(input("Informe o consumo médio do seu carro: "))

quantidade_litros = distancia_km / consumo_medio

print("A quantidade de Litros necesária para percorrer", distancia_km,"KM é:", quantidade_litros,"Litros")

print("****************")


preco_produto = float(input("Informe o valor da roupa: "))

percent_desconto = float(input("Informe o percentual de desconto: "))

valor_desconto = preco_produto * (percent_desconto/100) 

preco_final = preco_produto - valor_desconto

print("O valor final do produto é R$:", preco_final)

'''

qtd_moedas = 73

qtd_pessoas = int(input("Informe a quantidade de pessoas no grupo: "))

qtd_por_pessoa = int(qtd_moedas / qtd_pessoas)

sobra_bau = qtd_moedas % qtd_pessoas #resto da divisão

print(f"Cada pessoa recebe {qtd_por_pessoa} moedas.")

print(f"Sobram {sobra_bau} moedas no baú")