def solution(progresses, speeds):
    answer = []
    time = [(100 - progresses[i] -1) // speeds[i] +1  for i in range(len(progresses))]
    max_ = time[0]
    count = 1
    
    
    for i in range(1, len(time)):
        if max_ >= time[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_ = time[i] #max = time[i]로 재정의 됨
    
    answer.append(count)
    return answer    