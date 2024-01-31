import sys
input = sys.stdin.readline

# 명령어의 개수를 입력
n = int(input())

stack = []

for i in range(n):
    m = input().split()
    if m[0] == 'push':
        stack.append(int(m[1]))
    elif m[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
            
    elif m[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif m[0] == "empty":
        if len(stack) > 0 :
            print(0)
        else:
            print(1)
    
    elif m[0] == "size":
        print(len(stack))  
