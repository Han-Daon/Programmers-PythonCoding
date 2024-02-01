import sys
from collections import deque

n, k = map(int, input().split())

deq = deque([i for i in range(1,1+n)])

res = []
while len(deq) != 0:
    for _ in range(k-1):
        deq.append(deq.popleft())
    res.append(str(deq.popleft()))
    
print('<'+', '.join(res)+'>')