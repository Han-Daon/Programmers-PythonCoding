def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    if str_k in str_num:
        return str_num.index(str_k)+1
    else:
        return -1