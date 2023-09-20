# Classe Bola: crie uma classe que modele uma bola
# Atributos: Cor, circunferencia, material
# métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        print(f'A nova cor é: {self.cor}')

#Main
bola1 = Bola('Azul', 5, 'sintético')
bola1.trocaCor('Amarelo')
bola1.mostraCor()