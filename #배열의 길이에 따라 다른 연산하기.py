

def solution(arr, n):
    i = 0
    while i < len(arr):
        if len(arr) % 2 == 1: 
            if i % 2 == 0:      
                arr[i] += n
        else:                   
            if i % 2 == 1:      
                arr[i] += n
        i += 1                  
    return arr



# 컴프리헨션도 신경써보기
def solution(arr, n):
    return [x + n if (len(arr) % 2 == i % 2) else x for i, x in enumerate(arr)]