# FIFO - first in first out
# não é uma boa prática
# esse comportamento em uma lista grande traria problemas de performance, pois seria necessário percorrer toda a lista
# 
queue = []
queue.append('A')
print(queue)
queue.append('B')
print(queue)
queue.append('C')
print(queue.pop(0)) # o elemento removido é retornado
print(queue)