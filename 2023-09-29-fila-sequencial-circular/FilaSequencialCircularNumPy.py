import numpy as np
# Importa o módulo numpy para usar a classe np.full() para inicializar o array da fila.
# Numpy trabalha com arrays e matrizes multidimensionais em Python

class FilaException(Exception): # para capturar exceções levantadas pelos métodos da classe Fila; herda da classe base Exception
    def __init__(self,mensagem):
        super().__init__(mensagem)

class Fila:
# Define o construtor da classe Fila; inicializa o array da fila com o tamanho especificado pelo argumento size
# Aqui, um array NumPy é criado com o tamanho especificado (size) e inicializado com None em cada posição. O argumento dtype=object permite que o array armazene objetos Python de qualquer tipo
    def __init__(self, size:int=10):
        self.__array = np.full(size,None,dtype=object)
        self.__frente = 0  # indicando a posição do elemento na frente da fila
        self.__final  = -1 # indicando a posição do elemento no final da fila
        self.__tamanho = 0 # rastreando o número de elementos na fila
        
    def estaVazia(self)->bool:
        return self.__tamanho == 0

    def estaCheia(self)->bool:
        return self.__tamanho == len(self.__array)


    def __len__(self)->int: # retorna o tamanho da fila
        return self.__tamanho

    def elemento(self, posicao:int)->any: 
    # verifica se a posição na fila é válida e retorna o elemento na posição especificada
        try:
            assert self.estaVazia() == False, 'Fila está vazia'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para a fila com {len(self)} elementos'
            
            index = self.__frente
            for i in range(posicao-1):
                index = (index + 1)%len(self.__array)
            

            return self.__array[index]
        except AssertionError as ae:
            raise FilaException(ae)
                
    def busca(self, key:any)->int:
    # O método retorna o índice do elemento especificado na fila. 
    # O método verifica se o elemento está na fila e retorna o seu índice.
        index = self.__frente
        for i in range(len(self)):
            if self.__array[index] == key:
                return i+1
            index = (index + 1)%len(self.__array)
        raise FilaException(f'A chave {key} não está presente na fila')


    def enfileira(self, carga:any):
    # O método insere um elemento na fila. 
    # O método verifica se a fila está cheia e, se não estiver, insere o elemento no final da fila.
        try:
            assert not self.estaCheia(), 'Fila está cheia'
            
            # if self.__final == len(self.__array)-1:
            #     self.__final = 0
            # else:
            #     self.__final += 1

            self.__final = (self.__final + 1)% len(self.__array)

            self.__array[self.__final] = carga
            
            self.__tamanho += 1

        except AssertionError as ae:
            raise FilaException(ae)


    def desenfileira(self)->any:
    # O método remove um elemento da fila. 
    # O método verifica se a fila está vazia e, se não estiver, remove o elemento do início da fila
        try:
            assert not self.estaVazia(), 'Lista está vazia'

            carga = self.__array[self.__frente]

            self.__frente = (self.__frente + 1)% len(self.__array)
            self.__tamanho -= 1
            return carga
        except AssertionError as ae:
            raise FilaException(ae)  

        
    def __str__(self)->str:
        """ Método que retorna a ordenação atual dos elementos da pilha, do
            topo em direção à base

        Returns:
           str: a carga dos elementos da pilha, do topo até a base
        """  
        s = 'frente->[ '
        index = self.__frente
        for i in range(len(self)):
            s += f'{self.__array[index]}, '
            index = (index + 1)%len(self.__array)
        s = s.rstrip(', ')
        s += ' ]'
        return s

        

 

