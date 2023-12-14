<<<<<<< HEAD
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
=======
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
>>>>>>> 3f1bb2f19d28674dee2358ea1c183454ca2f9a25
    print(item)