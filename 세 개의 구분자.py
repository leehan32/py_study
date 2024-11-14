a = "abcd"


b =a.replace('a',' ')
c = b.replace('b', ' ')
d = c.replace('c', " ")

print(d.lstrip(" ").split(' '))