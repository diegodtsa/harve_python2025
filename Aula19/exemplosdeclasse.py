class Carro:
    def __init__(self, modelo, cor, ano, cidade):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.cidade = cidade

    def buzinar(self):
        print(f"Buzine {self.modelo}")

meu_carro = Carro('Marea', 'Amarelo', '1999', 'Paraná')

meu_carro.buzinar()



    


