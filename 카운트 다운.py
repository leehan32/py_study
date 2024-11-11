def solution(start_num, end_num):
    answer = []
    answer.extend(range(end_num,start_num+1))
    answer.sort(reverse= True)
    return answer