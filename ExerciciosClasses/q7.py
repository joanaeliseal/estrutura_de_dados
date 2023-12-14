"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade. 
b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, 
o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, 
um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser 
calculada a qualquer momento.
"""

class Tamagushi:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novoNome):
        self.nome = novoNome
        return self.nome
    
    def humor(self):
        if self.saude >=7 and self.fome >=5:
            return 'Está de bom humor'
        else:
            return 'Está de mau humor'

# main

bichinho = Tamagushi('Inho',0,0,0)    
bichinho.alterarNome('Juju')
bichinho.fome = 6
bichinho.saude = 4
bichinho.idade = 4

print('Nome:', bichinho.nome)
print('Idade:', bichinho.idade)
print('Humor:', bichinho.humor())