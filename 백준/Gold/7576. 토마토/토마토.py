import sys
from collections import deque

input= sys.stdin.readline

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

def solution():
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    for i in range(N):
        row = board[i]
        for j in range(M):
            if row[j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        cur = board[x][y]
        for k in range(4):
            nx = x+DX[k]
            ny = y+DY[k]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 0:
                board[nx][ny] = cur + 1 # 시간을 board에 직접 입력
                q.append((nx, ny))
    
    max_val = 1
    for row in board:
        if 0 in row:
            print(-1)
            return
        rmax = max(row)
        if rmax > max_val:
            max_val = rmax
    
    print(max_val - 1)

if __name__ == "__main__":
    solution()
