from SemaforoTemporizado import SemaforoTemporizado, Estado
from Temporizador import Temporizador


s1 = SemaforoTemporizado(Estado.Verde) # começa no estado "verde"
s2 = SemaforoTemporizado() # começa no estado "vermelho"

# print(s1.__dict__)
# print(s2.__dict__)

#Verificando o id de cada objeto
print('id:',id(s1))
print('id:',id(s2))

# Acionando o método get
print('S1:',s1.estadoAtual)
print(s1)
print(s1.tempoDeTransicao)
print('S2:',s2.estadoAtual)
print(s2)
print(s2.tempoDeTransicao)


s1.setup(2,4,6)
s1.start(2)
