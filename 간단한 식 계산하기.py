def solution(binomial):
    a= binomial.split()
    b = int(a[0])
    c = int(a[2])
    if '+'==a[1]:
        return b+c
    elif '-' == a[1]:
        return b-c
    elif '*' == a[1]:
        return b*c