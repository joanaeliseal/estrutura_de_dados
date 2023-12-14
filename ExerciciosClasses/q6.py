"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    
    def set_canal(self, canal):
        if canal >= 0 and canal <= 100:
            self.canal = canal
        else:
            print('Canal indisponível')
    
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
    
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

# Main
controle = TV(0, 25)
controle.set_canal(100)
controle.aumentar_volume()
controle.aumentar_volume()
controle.diminuir_volume()

print('Canal:', controle.canal)
print('Volume:', controle.volume)