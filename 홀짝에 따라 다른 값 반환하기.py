def solution(n):
    x = 0
    if n % 2 ==1:
        for i in range(1,n+1):
            if i % 2 != 0:
                x += i
    else:
        for i in range(1,n+1):
            if i % 2 != 1:
                x += i**2
                
                    
    return x



# 범위로 환산시 그냥 하면 0부터 시작 n-1 까지임
# 1부터 시작해서 n+1을 해야 내가 원하느 ㄴ값이 나옴


#다른사람 푼 문제

2
3
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)