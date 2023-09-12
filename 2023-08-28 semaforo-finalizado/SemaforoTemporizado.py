from Temporizador import Temporizador
from enum import Enum
from colors import Color

class Estado(Enum):
    Vermelho = 1
    Amarelo = 2
    Verde = 3


class SemaforoTemporizado:
    # definindo o construtor
    def __init__(self, estadoInicial:Estado = Estado.Vermelho):
        self.__estadoAtual = estadoInicial
        self.__timer = Temporizador()
        self.__tempoDeTransicao = {Estado.Verde:20,\
                                 Estado.Amarelo:5, \
                                 Estado.Vermelho:10}
    @property
    def estadoAtual(self)->Estado:
        return self.__estadoAtual

    @property
    def tempoDeTransicao(self)->dict:
        # Retornando uma cópia do objeto, e não sua referência
        # isso é importante para que o objeto não seja alterado
        return self.__tempoDeTransicao.copy()

    def __str__(self):
        return f'''
        +-----+
        | ({Color.vermelho("■") if self.__estadoAtual == Estado.Vermelho else " "}) |
        | ({Color.amarelo("■") if self.__estadoAtual == Estado.Amarelo else " "}) |
        | ({Color.verde("■") if self.__estadoAtual == Estado.Verde else " "}) |        
        +-----+'''


    def setup(self,tempoVermelho:int, tempoAmarelo:int, tempoVerde:int):
        '''
        Método que permite ajustar o tempo dos estados do semáforo.
        Aceita um tempo em segundos entre 1 e 59

        Argumentos
        ----------
        tempoVermelho(int): tempo em segundos de permanência no vermelho
        tempoAmarelo(int): tempo em segundos de permanência no amarelo
        tempoVerde(int): tempo em segundos de permanência no verde
        '''
        if tempoVermelho < 1 or tempoVermelho > 59:
            return
        elif tempoAmarelo < 1 or tempoAmarelo > 59:
            return
        elif tempoVerde < 1 or tempoVerde > 59:
            return

        self.__tempoDeTransicao[Estado.Vermelho] = tempoVermelho
        self.__tempoDeTransicao[Estado.Amarelo] = tempoAmarelo
        self.__tempoDeTransicao[Estado.Verde] = tempoVerde

    def __proximoEstado(self):
        if self.__estadoAtual == Estado.Vermelho:
            self.__estadoAtual = Estado.Verde
        elif self.__estadoAtual == Estado.Verde:
            self.__estadoAtual = Estado.Amarelo
        else:
            self.__estadoAtual = Estado.Vermelho


    def start(self, numCiclos:int):
        '''
        Método que inicia o ciclo de funcionamento do semáforo.

        Argumentos
        ----------
        numCiclos(int): número de ciclos que o semáforo deve executar.
                        Cada ciclo é constutuído pela passagem por 3 estados:
                        vermelho, amarelo e verde
        '''
        for i in range(numCiclos*3):
            print(self) 
            self.__timer.duracao = self.__tempoDeTransicao[self.__estadoAtual]
            self.__timer.ativar()
            self.__proximoEstado()
            print()
        