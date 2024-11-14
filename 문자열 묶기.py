def solution(strArr):
    answer = {}
    for i in strArr:
        a = len(i)
        answer[a] = answer.get(a, 0) + 1
    return max(answer.values())
