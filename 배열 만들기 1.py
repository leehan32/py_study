def solution(n, k):
    answer = [i for i in range(k, n + 1, k)] #범위설정할때 +1
    return answer