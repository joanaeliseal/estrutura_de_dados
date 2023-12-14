"""
Faça uma função recursiva chamada menores_rec() que receba como parâmetro um list de valores
numéricos e um número inteiro key. A função deve retornar quantos elementos da lista possuem
valor inferior a key. O protótipo da função é definido por:
def menores_rec( lista, key )
"""

def menores_rec(lista, key):
    if len(lista)==0:
        return 0
    elif lista[0] <= key:
        return 1 + menores_rec(lista[1:], key)
    else:
        return menores_rec[lista[1:], key]