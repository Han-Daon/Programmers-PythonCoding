def solution(arr):
    answer = []
    for i in range(len(arr)):#길이만큼 반복
        if [arr[i]] != arr[i + 1: i + 2]:
            answer.append(arr[i])
    return answer

# 추가로 알게 된 부분: 슬라이싱을 하면 [] 배열 값으로 나옴!
     - arr[:]  = [값]
     - 비교하는 값을 배열로 감싸줌: [arr[i]]
