
a = "aaaaa"
b = "bbbbb"






def solution(str1, str2):
    answer = ""
    
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
        
    return answer

print(solution(a,b))



#다른사람꺼
def solution(str1, str2):
    answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return answer