def solution(myString, pat):
    a = len(pat)
    b = myString.rfind(pat)
    answer = myString[:b+a]
    return answer



a="AbCdEFG"	
b= "dE"	



print(a.rfind("dE"))