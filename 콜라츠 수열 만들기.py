

a = 10


# 처음에 생각한거 와일문 을 자꾸 안써서 쓰는걸 잘모름 기억하기
def solution(n):
    answer = []
    while 1 == False:
        n % 2 ==0
        answer.append(n /2)
        n & 2 ==1
        answer.append(3* n +1)
    return answer

#정답
print(solution(a))

def solution(n):
    answer = []
    while n != 1:
        answer.append(n) 
        if n % 2 == 0:  
            n = n // 2 
        else:         
            n = 3 * n + 1   
    answer.append(1) 
    return answer
a = 10
print(solution(a)) 