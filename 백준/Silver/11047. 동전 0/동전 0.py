n , k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse = True)
result = 0

for i in coin:
    if k >= i:
        result += k//i
        k = k%i
        if k == 0:
            break
        
print(result)