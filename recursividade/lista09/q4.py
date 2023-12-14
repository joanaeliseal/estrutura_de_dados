"""Faça uma função recursiva chamada printInverse() que imprima uma string ao contrário."""

def printInverse(string):
    if not string:
        return
    else:
        print(string[-1], end=' ')
        printInverse(string[:-1])

nome = printInverse('Joana')
print(nome)