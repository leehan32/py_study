


print(ord('l'))

a = "abcdevwxyz"
a.replace(ord)



def solution(myString):
    answer = ''
    for i in myString:
        if ord(i) < ord('l'):
            i = 'l'
            answer += i
        else:
            answer +=i
    return answer