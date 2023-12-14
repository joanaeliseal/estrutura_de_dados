"""Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros. Se n = 3, a soma
seria igual a 1 + 2 + 3 = 6"""

def soma_numeros(n):
    if n == 0:
        return 0
    else:
        return n + soma_numeros(n-1)