def caixa_registradora():
    compras = {}
    total_compra = 0.0
    total_itens = 0

    while True:
        produto = input("Digite o nome do produto ou pressione enter para finalizar: ")

        if produto == "":
            break
        
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        preco = float(input(f"Digite o preço do {produto}: "))

        total_produtos = quantidade * preco
        total_compra += total_produtos
        total_itens += quantidade

        # Atualiza ou adiciona o produto no dicionario

        if produto in compras:
            compras[produto]["quantidade"] += quantidade
            compras[produto]["total"] += total_produtos
        else:
            compras[produto] = {
                "quantidade": quantidade,
                "preco_unitario": preco,
                "total":total_produtos
            }
    print("Resumo da Compra: ")
    for produto, info in compras.items():
        print(f"{produto}: {info['quantidade']} unidade(s) x R$ {info['preco_unitario']} = R${info['total']}")
    
    print(f"Total da Compra: R$ {total_compra}")
    print(f"Quantidade total de itens: {total_itens}")

caixa_registradora()