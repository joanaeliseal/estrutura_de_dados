"""Faça uma função recursiva chamada printstr() que imprima na tela uma string (caractere a
caractere na mesma linha)."""

def printstr(s, index=0):
    # Verifica se chegou ao final da string
    if index == len(s):
        return
    
    # Imprime o caractere atual sem quebra de linha
    print(s[index], end='')
    
    # Chama recursivamente a função para o próximo caractere
    printstr(s, index + 1)

# Exemplo de uso:
minha_string = "Hello, World!"
printstr(minha_string)