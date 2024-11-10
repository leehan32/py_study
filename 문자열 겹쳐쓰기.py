def solution(my_string, overwrite_string, s):
    x = len(overwrite_string)
    answer = my_string[:s]+overwrite_string+my_string[s+x:]
    return answer