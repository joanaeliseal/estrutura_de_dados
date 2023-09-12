class Pais:
    def __init__(self, nomePais, nomeCapital, dimensao:int):
        self.__nomePais = nomePais
        self.__nomeCapital = nomeCapital
        self.__dimensao = dimensao
        self.__listaFronteiras = []
    
    @property
    def listaFronteiras(self):
        return self.__listaFronteiras.copy()
    
    def addFronteira(self, pais:str):
        '''
        Adiciona um pais que faz fronteira com o objet em questao
        Argumentos
        -------------
        pais(str): o pais que vai ser adicionado como de fronteira

        Exceção
        -------------
        Lança um Exception() quando se tenta adicionar um país de fronteira
        que já está cadastrado
        '''
        if pais.title() not in self.__listaFronteiras:
            self.__listaFronteiras.append(pais.title())
        else:
            raise Exception(f'Pais {pais} já está registrado como fronteiriço com o {self.__nomePais}')

    def fazFronteiraCom(self, outroPais: 'Pais')->bool:
        return True if outroPais.__nomePais in self.__listaFronteiras else False

    def __str__(self):
        return f'{self.__nomePais},capital  {self.__nomeCapital}, {self.__dimensao} Km²'

