def solution(myString, pat):
    
    a =myString.replace('A','X').replace('B','A').replace('X','B')
    answer = int(pat in a)
    return answer














