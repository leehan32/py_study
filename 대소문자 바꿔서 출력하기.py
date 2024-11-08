str = input()
b = str.swapcase()
print(b)







#swapcase()없으면 이걸 쓸까?
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))