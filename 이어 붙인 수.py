def solution(num_list):
    
    answer1 = ''.join(str(num) for num in num_list if num%2==1)
    
    answer2 = ''.join(str(num) for num in num_list if num%2==0)
    
    return int(answer1) + int(answer2)