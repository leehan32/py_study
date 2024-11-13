b=[[2, 3], [0, 7], [5, 9], [6, 10]]
a= "rermgorpsam"
def solution(my_string, queries):
    answer = my_string
    for a,b in queries:
        answer = answer[:a]+answer[a:b+1][::-1]+answer[b+1:]
    return answer


print(solution(a,b))