import sys
from collections import deque

N = int(input())

def card(N):
    queue = deque(range(1,N+1))
    
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]

print(card(N))