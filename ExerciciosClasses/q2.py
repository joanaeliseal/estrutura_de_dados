# Classe Quadrado: Crie uma classe que modele um quadrado:
# 
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def mudar_lado(self, novoLado):
        self.lado = novoLado
            
    def area(self, lado, area):
        return (self.lado)**2

#main
quadrado1 = Quadrado(2)
quadrado1.mudar_lado(6)
quadrado1.area()
print(f'Valor do lado é: {quadrado1.mudar_lado()}')
print(f'A área é: {quadrado1.area()}')