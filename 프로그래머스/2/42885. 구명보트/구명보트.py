from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    people = deque(people)
    while people:
        if len(people) == 1 or people[0] + people[-1] > limit:
            people.popleft()  # 가장 무거운 사람을 보트에 태워 보내고
            answer += 1  # 보트의 수를 증가시킵니다.
        else:
            people.popleft()  # 가장 무거운 사람과 가장 가벼운 사람을 같이 태워 보내고
            people.pop()  # 두 사람을 리스트에서 제거합니다.
            answer += 1  # 보트의 수를 증가시킵니다.
    return answer
