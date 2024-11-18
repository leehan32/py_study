def solution(q, r, code):
    answer = ''
    for i in code:
        b =a[:q*i][r]
        answer += b
    return answer



a = "qjnwezgrpirldywt"


b =a[:q*i][r]


print(b)

def solution(q, r, code):
    answer = ''
    for i in range(len(code)):   
        if i % q == r:            
            answer += code[i]      
    return answer