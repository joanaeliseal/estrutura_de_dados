from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    #método é uma função que pertence à classe
    #parâmetro self é convenção começar por ele, e depois colocar os outros parametros 
    def __init__(self, nome, idade, comendo=False, falando=False): #init é o construtor
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return #apenas se a condição for verdadeira!
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
        if self.falando:
            print(f'{self.nome} não pode comer falando')
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return  #importante pois se não colocar, executa o q estiver abaixo
        print(f'{self.nome} parou de falar')
        self.falando = False

    def get_ano_nasc(self):
        return self.ano_atual - self.idade