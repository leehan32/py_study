def solution(my_string, target):
    a =my_string.lower()
    b =target.lower()
    answer = int(str(b) in str(a))
    return answer