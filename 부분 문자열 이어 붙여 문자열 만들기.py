

c=["progressive", "hamburger", "hammer", "ahocorasick"]
d=[[0, 4], [1, 2], [3, 5], [7, 7]]

def solution(my_strings, parts):
    answer = ""
    i =-1
    for a,b in parts:
        i += 1
        g=my_strings[i]
        answer += g[a:b+1]
        

    return answer


print(solution(c,d))