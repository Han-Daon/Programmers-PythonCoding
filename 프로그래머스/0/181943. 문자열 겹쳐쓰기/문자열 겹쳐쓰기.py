def solution(my_string, overwrite_string, s):
    answer = ''
    a = len(overwrite_string)
    answer = my_string[:s]+overwrite_string+my_string[a+s:]
    return answer