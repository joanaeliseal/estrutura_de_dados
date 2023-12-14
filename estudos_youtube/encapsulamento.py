"""
- Encapsulamento serve para proteger partes do código;
- Modificadores de acesso: public, protected, private
- Em python só tem publico e privado
- _ fraco; __ forte
"""

"""class BaseDeDados:
    def __init__(self):
        self.dados = {} #dicionário vazio
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome}) # atualiza o dicionario
    
    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]
"""
class BaseDeDados:
    def __init__(self):
        self._dados = {} #dicionário vazio
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome}) # atualiza o dicionario
    
    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.apaga_cliente(2)
bd.lista_clientes()