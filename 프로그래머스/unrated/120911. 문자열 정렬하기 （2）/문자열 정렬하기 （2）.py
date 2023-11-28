def solution(my_string):
    string = sorted(my_string.lower()) #sorted는 리스트를 반환함
    return ''.join(string) #문자열로 바꿔줘야함