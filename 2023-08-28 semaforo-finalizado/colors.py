class Color:
    '''
    Retorna a string colorida de verde, amarelo ou vermelho.

    Metodos:
    ---------------
    ANSI.verde(string : str)
    ANSI.amarelo(string : str)
    ANSI.vermelho(string : str)

    Argumentos
    ----------------
    string(str): A string a ser colorida.
    '''
    __RESET = "\033[0m"
    __VERDE = "\033[0;32m"
    __AMARELO = "\033[0;33m"
    __VERMELHO = "\033[0;31m"
    __AZUL = "\033[0;34m"
    __MAGENTA = "\033[0;35m"
    __WHITE = "\033[0;37m"


    @staticmethod
    def verde(string : str):
        return __class__.__VERDE + string + __class__.__RESET

    @staticmethod
    def amarelo(string : str):
        return __class__.__AMARELO + string + __class__.__RESET

    @staticmethod
    def vermelho(string : str):
        return __class__.__VERMELHO + string + __class__.__RESET

    @staticmethod
    def azul(string : str):
        return __class__.__AZUL + string + __class__.__RESET
    
    @staticmethod
    def magenta(string : str):
        return __class__.__MAGENTA + string + __class__.__RESET
    
    @staticmethod
    def branco(string : str):
        return __class__.__WHITE + string + __class__.__RESET
    
