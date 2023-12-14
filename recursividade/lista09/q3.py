"""Faça uma função recursiva chamada invertString() que retornte a sequência de caracteres de
uma string passada como argumento na ordem inversa"""

def invertString(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + invertString(string[:-1])
    
nome = invertString('Joana')
print(nome)