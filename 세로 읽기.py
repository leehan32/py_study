import textwrap

def solution(my_string, m, c):
    answer = ""
    slice = textwrap.wrap(my_string,m)
    for i in slice:
        answer += i[c-1]
    return answer


#다른사람풀이
def solution(s, m, c):
    return s[c-1::m]