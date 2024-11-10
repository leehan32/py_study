my_string	
overwrite_string	
s	result
"He11oWor1d"	"lloWorl"	2



def solution(my_string, overwrite_string, s):
    b = len(my_string)
    a = len(overwrite_string)
    my_string[s:s+a] = a[:]
    return my_string