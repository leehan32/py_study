def solution(n_str):
    answer =1
    if len(n_str)>=11:
        return sum(n_str)
    else:
        for i in n_str:
            answer =1
            answer = answer *i
        return answer
        




# prod -> 리스트 안의 모든 걸 곱하는 함수

from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)