queue = []
queue.append(1)
queue.append(2)
queue.pop(0)  # Removes 1


#using collections.deque
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # Removes 1
