def solution(myStr):
    b =myStr.replace('a',' ')
    c = b.replace('b', ' ')
    d = c.replace('c', " ")
    words = d.strip().split()
    if not words:
        return ["EMPTY"]
    return words

