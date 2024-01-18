def solution(arr):
    answer = []
    for i in range(len(arr)):#길이만큼 반복
        if [arr[i]] != arr[i + 1: i + 2]:
            answer.append(arr[i])
    return answer