def solution(arr, n):
    answer = []
    if len(arr) % 2 ==0:
        answer = arr[::2] +n
    else:
        answer = arr[1::2]+n
    return answer