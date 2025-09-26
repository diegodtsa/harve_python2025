ano = int(input("Informe o ano para descobrir a idade histórica: "))
sigla = input("Digite 'a.c' para antes de Cristo e 'd.c' para depois de Cristo:").lower

if sigla == "a.c":
    ano_ajustado = -ano
else:
    if sigla == "d.c":
        ano_ajustado = ano
    else:
        ano_ajustado = None
        print("Valor Incorreto: Digite 'a.c' para antes de Cristo e 'd.c' para depois de Cristo:")

if ano_ajustado is None:
    idade_historica = "Valor Incorreto"
    print(f"{idade_historica}")
else:
    if ano_ajustado <= -4000:
        idade_historica = "Pré Histórica"
        print(f"O ano {ano} {sigla} pertence ao período: {idade_historica}")
    else:
        if -4000 < ano_ajustado <= 476:
            idade_historica = "Antiguidade"
            print(f"O ano {ano} {sigla} pertence ao período: {idade_historica}")
        else:
            if 476 < ano_ajustado <= 1453:
                idade_historica = "Idade Média"
                print(f"O ano {ano} {sigla} pertence ao período: {idade_historica}")
            else:
                if 1453 < ano_ajustado <= 1789:
                    idade_historica = "Idade Moderna"
                    print(f"O ano {ano} {sigla} pertence ao período: {idade_historica}")
                else:
                    if ano_ajustado > 1789:
                        idade_historica = "Idade Contemporanêa"
                        print(f"O ano {ano} {sigla} pertence ao período: {idade_historica}")
                    else:
                        idade_historica = "Ano Inválido"
                        print(f"{idade_historica}")
    