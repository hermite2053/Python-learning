# collections: Container Datatypes
# deque -- double-ended queue
from collections import deque

queue = deque(['beta','gamma', 'delta'])
print(queue)

queue.append('epsilon')
print(queue)

queue.appendleft('alpha')
print(queue)

queue.pop()
print(queue)

queue.popleft()
print(queue)

