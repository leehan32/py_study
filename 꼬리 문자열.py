

def solution(str_list, ex):
    answer = ""
    for i in str_list:
        if ex not in i:  #ex가 i안에 있어야했음 idp str_list쓰고 한참해맴
            answer += i  
    return answer





#다른사람 람다 쓴거 구경
def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))