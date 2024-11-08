


def solution(num_list):
    a = 1
    b = sum(num_list)**2
    for i in num_list:
        a *= i
    if a>b:
        return 0
    elif a<b:
        return 1
    
    
        

# 다른사람 꺼 for안에 두번 돌리기 가능 알아두기

def solution(num_list):
    a=1
    b=0
    for x in num_list:
        a*=x
        b+=x
    if a<b*b: return 1
    return 0