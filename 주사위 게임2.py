def solution(a, b, c):
    if (a != b) and (b != c) and (a != c):  
        return a + b + c
    elif (a == b and b != c) or (b == c and c != a) or (a == c and c != b):  
        return (a+b+c)*(a**2 + b**2 + c**2)
    else:  
        return (a+b+c)*(a**2 + b**2 + c**2)*(a**3 + b**3 + c**3)
    
    



    #다른 사람의 풀이 set으로 중복값을 골라내고 중복값이 세개면 len의 요소가 1개 두개면 2개 
    #이런식으로 찾아서 사용 가능 중복값 제거시 셋도 활용하는거 생각해보자

def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
    

    #내가 쓴거랑 비슷해보여도 훨씬 간단하고 직관적
    def solution(a, b, c):
    answer=a+b+c
    if a==b or b==c or a==c: answer*=a**2+b**2+c**2
    if a==b==c:answer*=a**3+b**3+c**3
    return answer