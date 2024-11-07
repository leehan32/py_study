def solution(num_list, n):
    answer = int(n in num_list)
    return answer


#다른 사람 깔끔해 보이는 코드
def solution(num_list, n):
    return 1 if n in num_list else 0