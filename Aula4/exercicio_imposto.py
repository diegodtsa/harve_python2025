valor_renda = (float(input("Informa o valor da Renda: ")))

if valor_renda <= 2259.20:
    grupo = "Você está Isento de Imposto"
elif valor_renda >= 2259.21 and valor_renda <= 2826.65:
    grupo = "Sua Aliquota é de 7.5% você deve pagar R$ 169, 44"
elif valor_renda >=2826.66 and valor_renda <= 3751.05:
    grupo = "Sua Aliquota é 15% você deve pagar R$ 381, 44"
elif valor_renda >= 3751.06 and valor_renda <= 4664.68:
    grupo = "Sua Aliquota é 22.5% você deve pagar R$ 662,77"
elif valor_renda > 4664.68:
    grupo = "Sua Aliquota é 27.5% você deve pagar R$ 896,00"

print(grupo)
