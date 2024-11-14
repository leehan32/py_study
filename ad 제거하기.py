def solution(strArr):
    answer = []
    휴지통 = []
    for i in strArr:
        if "ad" in i:
            휴지통.append(i)
        else:
            answer.append(i)
    return answer