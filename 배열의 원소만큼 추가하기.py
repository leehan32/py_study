def solution(arr):
    answer = []
    for i in arr:
        answer.extend([i] * i)
        
    return answer



arr =[5, 1, 4]

print(solution(arr))