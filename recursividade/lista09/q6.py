"""Faça uma função recursiva chamada ispalindrome() que retorne verdadeiro caso uma string seja
palíndrome, ou falso caso contrário."""

def isPalindrome(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    
    return isPalindrome(s[1:-1])

palavra = isPalindrome('radar')
print(palavra)