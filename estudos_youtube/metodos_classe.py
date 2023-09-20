# Método de Instância vs Método de Classe

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        print(self.ano_atual - self.idade)


    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc): # cls é convenção, refere-se a classe
        idade = cls.ano_atual - ano_nasc
        # idade é variável sem o self; só está disponivel no escopo do método; acesso as variaveis, atributos da classe
        # metodo deve retornar o objeto da classe
        return cls(nome, idade)
    
# p1 = Pessoa.por_ano_nasc('Luiz', 1987)
p1 = Pessoa('LUIZ', 36)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nasc()

# O método é relacionado a classe ou a instancia?