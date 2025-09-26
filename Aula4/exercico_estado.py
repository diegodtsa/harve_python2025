estado_usuario = input("Informe o estado onde você mora: ").upper()
if estado_usuario == "PARANÁ" or estado_usuario == "SANTA CATARINA" or estado_usuario == "RIO GRANDE DO SUL":
    print("Você mora no Sul do Brasil")
else:
    print("Você não mora no Sul do Brasil")