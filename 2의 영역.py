def solution(arr):
    idx_list = [i for i, x in enumerate(arr) if x == 2]
    if not idx_list:
        return [-1]
    return arr[min(idx_list):max(idx_list)+1]