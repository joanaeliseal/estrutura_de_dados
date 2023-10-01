from collections import deque
from typing import Deque, Any

queue: Deque[Any] = deque()
queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')

print('Removido:', queue.popleft())

print('For inútil')
for item in queue:
    print(item)