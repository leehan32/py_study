def solution(myString):
    answer = []
    a= myString.replace('x'," ").split(" ")
    for i in a:
        answer.append(len(i))


    return answer

