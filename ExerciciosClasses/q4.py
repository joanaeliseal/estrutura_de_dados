# Classe Pessoa: Crie uma classe que modele uma pessoa:
# 
# Atributos: nome, idade, peso e altura
# Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, ano):
        self.ano = ano
        self.idade += ano

    def engordar(self, balanca):
        self.peso += balanca

    def emagrecer(self, balanca):
        self.peso -= balanca

    def crescer(self, altura, ano):
        self.idade += ano
        if self.idade < 21:
            cresce = 0.05*altura
            self.altura += cresce
        else:
            return self.altura
        
#main

pessoa = Pessoa('Joana', 27, 57, 1.60)

pessoa.envelhecer(8)
pessoa.engordar(6)
pessoa.emagrecer(4)
pessoa.crescer(2)

print(f'''A pessoa {pessoa.nome}: 
      \nEnvelheceu: {pessoa.envelhecer()}
    \nEngordou: {pessoa.engordar()}
    \nEmagreceu: {pessoa.emagrecer()}
    \nCresceu: {pessoa.crescer()}
      ''')