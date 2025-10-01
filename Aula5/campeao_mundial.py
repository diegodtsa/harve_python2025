campeoes_mundiais = [
    "1930 - Uruguai",
    "1934 - Itália" ,
    "1938 - Itália",
    "1950 - Uruguai",
    "1954 - Alemanha Ocidental",
    "1958 - Brasil", 
    "1962 - Brasil", 
    "1966 - Inglaterra", 
    "1970 - Brasil", 
    "1974 - Alemanha Ocidental", 
    "1978 - Argentina",
    "1982 - Itália",
    "1986 - Argentina", 
    "1990 - Alemanha Ocidental",
    "1994 - Brasil", 
    "1998 - França", 
    "2002 - Brasil", 
    "2006 - Itália",
    "2010 - Espanha", 
    "2014 - Alemanha", 
    "2018 - França",
    "2022 - Argentina"
]

time_consulta = input("Digite o time para verificar quantas vezes ele foi campeão mundial: ")

num_titulos = 0

for campeao in campeoes_mundiais:
    ano,time = campeao.split(" - ")
    if time == time_consulta:
        num_titulos += 1
    if num_titulos == 1:
        titulo = "Campeão(ã)"
    elif num_titulos == 2:
        titulo = "Bi-Campeão(ã)"
    elif num_titulos == 3:
        titulo = "Tri-Campeão(ã)"
    elif num_titulos == 4:
        titulo = "Tetra Campeão(ã)"
    elif num_titulos == 5:
        titulo = "Penta Campeão(ã)"
    elif num_titulos == 6:
        titulo == "Hexa Campeão(ã)"

if num_titulos > 0:
    print(f"A Seleção do(a) {time_consulta} foi campeão(ã) mundial {num_titulos} vez(es)!, ela é {titulo} Mundial")
else:
    print(f"A Seleção do(a) {time_consulta} não ganhou nenhum Campeonato Mundial")
