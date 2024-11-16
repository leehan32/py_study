


a="apporoograpemmemprs"
b=[1, 16, 6, 15, 0, 10, 11, 3]


def solution(my_string, indices):
    answer = (x for x in my_string if x != my_string[indices])
    return answer

#
print(str(solution(a,b)))
#위에 리스트안에로는 인덱싱불가능 에누머레이트로 키값처럼 변환하여 특정 키값의 수가 리스트에있으면 빠지게함
def solution(my_string, indices):
    
    return ''.join(char for i, char in enumerate(my_string) if i not in indices)