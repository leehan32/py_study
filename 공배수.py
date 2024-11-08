def solution(number, n, m):
    x = number%n 
    y= number%m
    if x == 0 and y==0:
        return 1
    else:
        return 0
