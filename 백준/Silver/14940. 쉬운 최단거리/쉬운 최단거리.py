import sys
from collections import deque

input = sys.stdin.readline
DX = (1, -1, 0, 0)
DY = (0, 0, 1, -1)

def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    sr = sc = -1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                board[i][j] = -1         
            elif board[i][j] == 2:
                sr, sc = i, j

    q = deque([(sr, sc)])
    board[sr][sc] = 0                    

    while q:
        x, y = q.popleft()
        cur = board[x][y]
        for k in range(4):
            nx = x + DX[k]
            ny = y + DY[k]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == -1:
                board[nx][ny] = cur + 1
                q.append((nx, ny))

    for row in board:
        print(*row)

if __name__ == "__main__":
    solution()
