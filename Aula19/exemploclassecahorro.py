class Cachorro:
    def __init__(self,nome, raca, porte, idade):
        self.nome = nome
        self.raca = raca
        self.porte = porte
        self.idade = idade
    
    def latir(self):
        print(f"O {self.nome} esta latindo, ele tem {self.idade} ano !")
    
    def sentar(self):
        print(f"O {self.nome} esta sentado !")
    
    def comer(self):
        print(f"O {self.nome} esta comendo !")
    
    def passear(self):
        print(f"O {self.nome} esta passeado !")

meu_cachorro = Cachorro('Bolinha','Vira-Lata','Médio', 1)

meu_cachorro.latir()
meu_cachorro.sentar()
meu_cachorro.comer()
meu_cachorro.passear()
        