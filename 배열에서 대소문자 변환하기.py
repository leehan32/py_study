
def solution(strArr):
    return [word.upper() if i % 2 == 1 else word.lower() for i, word in enumerate(strArr)]




#비슷한거 같지은데 

def solution(strArr):
    return [strArr[i].lower() if i%2 == 0 else strArr[i].upper() for i in range(0, len(strArr))]
