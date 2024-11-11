def solution(n_str):
    answer =1
    if len(n_str)>=11:
        return sum(n_str)
    else:
        for i in n_str:
            
            answer = answer *i
        return answer