def solution(num_list):
    answer = 0
    negative =0
    for i in num_list:
        if i > 0:
            answer += 1
        elif i< 0:
            negative += 1
            break
    if negative == 0:
        return-1   
    return answer

