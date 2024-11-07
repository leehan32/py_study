# def solution(numbers, n):
#     answer = 0
#     for i in numbers:
#         answer += i
#         if answer > n:
#             return answer 
    


# #다른 사람들 푼 예시 next는 어떻게 쓰는 걸까?
# def solution(numbers, n):
#     return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)


# a =[34, 5, 71, 29, 100, 34]

# print(solution(a,139))

numbers = [i for i in range(1, 101)]

def sol(numbers, n):
    return next(numbers[i] for i in range(len(numbers)) if numbers[i] > 30)

print(sol(numbers, 30))