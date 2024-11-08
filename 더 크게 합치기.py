def solution(a, b):
    x = str(a)
    y = str(b)
    z = int(x+y)
    b = int(y+x)
    if z > b:
        return z
    elif z<b:
        return b
    else:
        return z
    



    # 다른 사람 풀이 포매팅으로더 간단히 함

def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))