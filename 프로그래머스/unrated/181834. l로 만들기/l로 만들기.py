def solution(myString):
    answer = ''
    for char in myString:
        if ord('l') >= ord(char):
            answer += 'l'
        else:
            answer += char
    return answer