# def solution(arr):
#     for i in len(arr):
#         for j in len(a[:])
#             if arr[i][j] == arr[j][i]:
#                 return 1
#             else:
#                 return 0
        



# a = [[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]


# r또는을 제외하면 나머지 가 아닌경우 1이 리턴됨


def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
            #else:                  #엘스빼고 리턴을 한단게 밖으로
            return 1
            


print(solution(a))




#다른사람 풀이
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))


#zip은 튜플형태로 전치되어나옴 다시 리스트를 씌워서 바꾸긴했음
#맵으로 zip(튜플)로 나온 형태를 리스트로 바꾸고 다시 리스트를 써서 2차원 배열로 바꿈