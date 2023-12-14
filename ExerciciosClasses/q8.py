"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
e pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, criando pelo menos dois macacos, 
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = [] # inicializa com bucho vazio; lista vazia.

    def comer(self, alimento):
        self.bucho.append(alimento) # adiciona os alimentos ao bucho

    def verBucho(self):
        return self.bucho
    
    def digerir(self):
            if len(self.bucho) > 0:
                self.bucho = []  # Esvazia o estômago após a digestão.
            else:
                return f"{self.nome} não tem nada no estômago."

# main

# Criando dois macacos
macaco1 = Macaco("Jorge")
macaco2 = Macaco("Claudio")

# Alimentando os macacos com 3 alimentos diferentes
macaco1.comer("Banana")
macaco2.comer("Maçã")
macaco1.comer("Pêssego")

# Verificando o conteúdo do estômago
print(f"{macaco1.nome} tem no estômago: {macaco1.verBucho()}")
print(f"{macaco2.nome} tem no estômago: {macaco2.verBucho()}")

# Digerindo
macaco1.digerir()
macaco2.digerir()

# Verificando o estômago após a digestão
print(f"{macaco1.nome} tem no estômago: {macaco1.verBucho()}")
print(f"{macaco2.nome} tem no estômago: {macaco2.verBucho()}")