from collections import Counter

def solution(array):
    counter = Counter(array)
    mode = counter.most_common() 
    if len(mode) > 1 and mode[0][1] == mode[1][1]: 
        return -1
    return mode[0][0] 