"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

class ContaCorrente:
    def __init__(self, nome, conta, saldo=0.0):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
        

    def alterarNome(self, nome):
        self.nome = nome
        return self.nome
    
    def deposito(self, dinheiro)->float:
        self.saldo += dinheiro
        return self.saldo
    
    def saque(self, dinheiro):
        self.saldo -= dinheiro
        return self.saldo
    
#main

cliente = ContaCorrente('Joana', 1313)
cliente.alterarNome('Bia')
cliente.deposito(100)
cliente.saque(10)
print(cliente.nome)
print('Saldo:', cliente.saldo)