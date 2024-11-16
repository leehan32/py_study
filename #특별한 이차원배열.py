import numpy as np

def solution(n):
    
    return np.eye(n)





print(solution(3))



#다른사람 풀은거 댓글보니 넘파이 없이 구현하는게 코테에서 나옴 확인해보기

def solution(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]