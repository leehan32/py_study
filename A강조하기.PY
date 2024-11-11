def solution(myString):
    answer = ""
    for i in myString:
        if i =='a'or i =="A":# 'a' or 'A' 로했었는데 이게 둘을비교해서 참이라인식 else로 안빠짐
            answer += i.upper()
        else:
            answer += i.lower()
    return answer





#리플레이스 좀더 생각해 보자
def solution(myString):
    return myString.lower().replace('a', 'A')