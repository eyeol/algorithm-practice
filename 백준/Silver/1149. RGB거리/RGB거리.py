import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    board = []
    for _ in range(N):
        r, g, b = map(int, input().split())
        board.append((r, g, b))
    
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = board[0]

    for i in range(1, N): # 1부터 N-1까지
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + board[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + board[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + board[i][2]
    
    print(min(dp[N-1]))



if __name__ == "__main__":
    solution()