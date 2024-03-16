n = int(input())
people = list(map(int, input().split()))

people.sort()
answer = 0

for i in range(1,n+1):
    answer +=sum(people[0:i])#0번째 수부터 i번째 숙까지를 더함
print(answer)
    