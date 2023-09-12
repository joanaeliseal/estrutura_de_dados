class ContaCorrente:
    def __init__(self,numero: int, nomeTitutar:str,saldo: float = 0) -> None:
        self.__numero = numero
        self.__nomeTitutar = nomeTitutar
        self.__saldo = saldo

    @property
    def numero(self) -> int:
        return self.__numero
    
    @property
    def nomeTitutar(self) -> str:
        return self.__nomeTitutar
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    def depositar(self,valor: float) -> None:
        self.__saldo += valor

    def sacar(self,valor: float) -> None:
        if valor > self.__saldo:
            return False
        else:
            self.__saldo -= valor
            return True