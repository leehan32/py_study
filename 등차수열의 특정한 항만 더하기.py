
a = 3
d = 4
included= [True, False, False, True, True]


def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        b = a +(i * d)
        if included[i]:
            answer += b
    return answer
    

print(solution(a,d,included))




#다른 사람 풀이1
2
3
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)


#예 불리언 표현에 에누머레이트를 적용하면 if f 한문장으로 실행을 걸러낼 수 있음