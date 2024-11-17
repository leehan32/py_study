




def solution(picture, k):
    answer = []
    for i in picture:
        for j in i:

            answer += j*k
        return answer


a = ["x.x", ".x.", "x.x"]


print(solution(a,3))