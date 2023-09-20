# Classe Retangulo: Crie uma classe que modele um retangulo:
# 
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valor(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
    
    def retornar_mudar_valor(self):
        return self.base, self.altura

    def area(self, base, altura):
        return base * altura
    
    def perimetro(self, base, altura):
        return 2(base+altura)
    
#main

base = int(input('Base: '))
altura = int(input('Altura: '))

formula = Retangulo(base, altura)

print(f'Área: {formula.area():.1f}')
print(f'Perímetro: {formula.perimetro():.1f}')
print(f'Serão necessários {formula.area():.1f} pisos e {formula.perimetro():.1f} para rodapés')