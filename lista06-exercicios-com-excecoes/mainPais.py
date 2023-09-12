from pais import Pais

pais1 = Pais('Alemanha', 'Berlin', 200000000)
print(pais1.listaFronteiras)

pais2 = Pais('França', 'Paris', 125615325761)
print(pais2.listaFronteiras)

print(pais1.fazFronteiraCom(pais2))
try:
    pais1.addFronteira('Austria')
    pais1.addFronteira('Polonia')
    pais1.addFronteira('AUSTRIA')    
except Exception as e:
    print(e)

print(pais1.listaFronteiras)

print('Fim do programa')