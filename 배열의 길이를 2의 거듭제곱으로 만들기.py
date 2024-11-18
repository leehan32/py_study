def solution(arr):
    a = len(arr)
    b = 1
    while b < a:
        b *= 2
    return arr + [0] * (b - a)