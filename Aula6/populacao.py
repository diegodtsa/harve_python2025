def consulta_populacao():
     capitais_populacao = {
        "Buenos Aires": 15.2,
        "Sucre": 0.36,
        "Brasília": 4.7,
        "Santiago": 6.8,
        "Bogotá": 7.4,
        "Quito": 2.7,
        "Georgetown": 0.12,
        "Assunção": 0.52,
        "Lima": 10.7,
        "Paramaribo": 0.24,
        "Montevidéu": 1.7,
        "Caracas": 2.9
    }

capital = input("Digite o nome da capital da América do Sul: ").title()

populacao = capitais_populacao.get(capital)

if populacao == None:
    print("Capital não encontrada! ")
else:
    print(f"A população de {capital} e aproximadamente {populacao}")

consulta_populacao()