def solution(num_list):
    a = num_list[-1]
    b = num_list[-2]
    if a >b:
        
        return num_list + [a-b]
    else:
        return num_list + [a*2]
    
    
    
