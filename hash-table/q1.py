"""
1) Encapsule as propriedades internas da classe ChainHashTable. Torne o método hash() privado.
"""
import numpy as np

import numpy as np

class Encadeamento:
    def __init__(self, tamanho=10):
        self.__ocupados = 0
        self.__tamanho = tamanho
        self.__tabela = np.full(tamanho, None)

    def __hash(self, chave):
        # função hash modular
        return hash(chave) % self.__tamanho
    
    def __rh(self, index):
        return (index + 1) % len(self.__tabela)
    
    def estaCheia(self):
        return self.__ocupados == len(self.__tabela)

    def inserir(self, chave, valor):
        if self.estaCheia():
            return False
        index = self.__hash(chave)

        while self.__tabela[index] is not None:
            index = self.__rh(index)
            print(index)

        self.__tabela[index] = valor
        self.__ocupados += 1
        return True

    def busca(self, chave):
        index = self.__hash(chave)
        if self.__tabela[index] is not None:
            return self.__tabela[index]
        return None

    def delete(self, chave):
        index = self.__hash(chave)
        if self.__tabela[index] is not None:
            self.__tabela[index] = None
            self.__ocupados -= 1

# Criando uma instância da classe
hash_table = Encadeamento(10)

# Inserindo valores
hash_table.inserir('a', 1)
hash_table.inserir('b', 2)
hash_table.inserir('c', 3)
print(hash_table.__dict__)

# Imprimindo valores
print(hash_table.busca('a'))  # 1
print(hash_table.busca('b'))  # 2
print(hash_table.busca('c'))  # 3

# Excluindo valor
hash_table.delete('b')

# Tentando acessar valor excluído
print(hash_table.busca('b'))  # None

