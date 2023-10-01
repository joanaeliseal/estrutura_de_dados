from __future__ import annotations
from typing import Any

EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'

class EmptyFilaError(Exception):
    ...
    

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node
        
    def __repr__(self) -> str:
        return f'{self.value}'
    
    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)

class Fila:
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0

    def adicionar(self, nodeValue: Any) -> None:
        new_node = Node(nodeValue)

        if not self.first:
            self.first = new_node

        if not self.last:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self._count += 1

    def remover(self) -> None:
        if not self.first:
            raise EmptyFilaError('Fila Vazia')
        
        first = self.first
        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_NODE_VALUE)

        self._count -= 1
        return first
    
    def mostrar_elemento(self) -> Node:
        return self.first

    # implementação de padrões de Python abaixo:

    def __len__(self) -> int:
        return self._count
    
    def __bool__(self) ->bool:
        return bool(self._count)
    
    def __iter__(self) -> Fila:
        return self
    
    def __next__(self) ->Any:
        try:
            nextValue = self.pop()
            return nextValue
        except EmptyFilaError:
            raise StopIteration
    def __repr__(self) -> str:
        if not self.first:
            return 'Fila()'
        return f'Fila: {self.first, self.last}'
        
# main
if __name__ == "__main__":
    queue = Fila()
    queue.adicionar('A')
    queue.adicionar('B')
    queue.adicionar('C')

    print('Fora do for', next(queue))

    for item in queue:
        print(item)