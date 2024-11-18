

#이거 그냥 들어가니깐 적혀있어서 제출해보니 정답
#나중에 다시 해보기

















def solution(a, b, c, d):
    # 숫자들을 리스트로 만들어서 처리하기 쉽게 함
    nums = [a, b, c, d]
    # 각 숫자가 몇 번 나왔는지 카운트
    counter = {}
    for n in nums:
        counter[n] = counter.get(n, 0) + 1
    
    # 서로 다른 숫자의 개수
    different_nums = len(counter)
    
    # 1. 모든 숫자가 같은 경우 (different_nums == 1)
    if different_nums == 1:
        return 1111 * a
    
    # 2. 두 가지 숫자가 있는 경우 (different_nums == 2)
    elif different_nums == 2:
        # 3:1로 나뉘는 경우
        if 3 in counter.values():
            p = [num for num, count in counter.items() if count == 3][0]
            q = [num for num, count in counter.items() if count == 1][0]
            return (10 * p + q) ** 2
        # 2:2로 나뉘는 경우
        else:
            p, q = counter.keys()
            return (p + q) * abs(p - q)
    
    # 3. 세 가지 숫자가 있는 경우 (different_nums == 3)
    elif different_nums == 3:
        # 2:1:1로 나뉘는 경우
        p = [num for num, count in counter.items() if count == 2][0]
        q, r = [num for num, count in counter.items() if count == 1]
        return q * r
    
    # 4. 네 숫자가 모두 다른 경우 (different_nums == 4)
    else:
        return min(nums)