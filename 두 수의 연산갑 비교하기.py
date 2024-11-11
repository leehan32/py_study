
a = 2
b = 91
x = int(''.join(str(a)+str(b)))
def solution(a, b):
    x = int(''.join(str(a)+str(b)))
    y = 2 * a * b
    if x > y:
        return x
    elif x<y:
        return y
    else:
        x
   




# 다른 사람풀이  간단,명료 하네요
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)