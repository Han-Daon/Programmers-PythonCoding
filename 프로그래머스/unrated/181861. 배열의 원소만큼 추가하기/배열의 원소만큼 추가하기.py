def solution(arr):
    answer = []
    
    for i in arr: #배열에 있는 수를 잡기
        for a in range(i): #i를 a로 받고 i만큼 반복 해서 끝에 추가해라
            answer.append(i)
        
    return answer