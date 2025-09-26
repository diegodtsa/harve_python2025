sementes = input("O Vegetal possui sementes ?: (sim/não)").lower()
flores = input("O Vegetal possui flores?: (sim/não)").lower()
reproducao = input("A reprodução do Vegetal depende de água?: (sim/não)").lower()
frutos = input("O Vegetal possui frutos?: (sim/não)").lower()
vaso_condutores = input("O vegetal possui vasos condutores?: (sim/não)").lower()

if sementes == "não" and flores == "não" and reproducao == "sim" and frutos == "não" and vaso_condutores == "não":
    grupo = "O Vegetal é uma briofita do grupo Criptrogramas"
elif sementes == "não" and flores == "não" and reproducao == "sim" and frutos == "não" and vaso_condutores == "sim":
    grupo = "O Vegetal é uma Pteridófitas do grupo Criptrogramas"
elif sementes == "sim" and flores == "sim" and reproducao == "sim" and frutos == "não" and vaso_condutores == "sim":
    grupo = "O Vegetal é uma Gimnospermas do grupo Fanerógramas"
elif sementes == "sim" and flores == "sim" and reproducao == "sim" and frutos == "sim" and vaso_condutores == "sim":
     grupo = "O Vegetal é uma Angiospermas do grupo Fanerógramas"
else:
    grupo = "Vegetal Desconhecido"

print(grupo)