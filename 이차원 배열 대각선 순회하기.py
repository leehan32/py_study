def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] > k:

                answer += board[i][j]
    return answer

# 부등호 잘못봐서 시간배림
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):  
            if i + j <= k:              
                answer += board[i][j]
    return answer