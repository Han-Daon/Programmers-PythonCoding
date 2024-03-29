def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    answer = n - len(set_lost)
    
    for i in set_lost:
        if i-1 in set_reserve:
            answer += 1
            set_reserve.remove(i-1)
        elif i+1 in set_reserve:
            answer += 1
            set_reserve.remove(i+1)
            
    return answer