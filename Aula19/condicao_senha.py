

senha_correta = "python123"

tentativa = ""

while tentativa != senha_correta:
    tentativa = input("Informe a senha: ")
    if tentativa != senha_correta:
        print("Senha Incorreta")
    else:
        print("Senha Correta")
        