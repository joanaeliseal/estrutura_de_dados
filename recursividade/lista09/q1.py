"""Faça uma função recursiva chamada recursiveLength() que retorne a quantidade de caracteres
de um string."""

def recursiveLength(string):
    if len(string) == 0:
        return 0
    else:
        return 1 + recursiveLength(string[1:])
    
nome = recursiveLength('Joana')
print(nome)