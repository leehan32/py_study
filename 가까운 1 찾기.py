# def solution(arr, idx):
#     answer = 0
#     return answer


#원본 리스트 컴프리핸션으로 되겠다는 생각은 했는데 뒤조건을 제대로
#적어내지 못함

max[x for x in range(len(arr) if x > idx)]




#바꾼후 인덱스 보다 큰지 확인하고 해당위치 값이 1인지를 교집합으로 판별
a = [i for i in range(len(arr)) if i >= idx and arr[i] == 1]

#값이 없으면 -1
min(a) if a else -1




# 다른사람 트라이 익셉으로 활용



def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx) #인덱스 이용 값을 1을 찾되 idx위치 부터 시작하라는 의미)
    except:
        answer = -1

    return answer