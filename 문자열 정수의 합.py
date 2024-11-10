

x = "123456789"

def solution(num_str):
    a = 0
    for i in (num_str):
        a += int(i)
    return a




print(solution(x))



#map 함수 활용도 도 잘 봅시다

def solution(num_str):
    return sum(map(int, num_str))



print(solution(x))




