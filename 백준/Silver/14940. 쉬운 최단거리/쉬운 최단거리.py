import sys
from collections import deque

input= sys.stdin.readline

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 도달못한 위치 확인 위해 visited 필요
    visited = [[0 for _ in range(M)] for _ in range(N)]

    r = 0
    c = 0
    # 목표지점 확인
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                r = i
                c = j

    q = deque([(r, c)])
    board[r][c] = 0
    visited[r][c] = 1

    while q:
        x,y = q.popleft()
        cur = board[x][y]
        for k in range(4):
            nx = x + DX[k]
            ny = y + DY[k]
            # 범위 안에 있고 갈 수 있는 땅이면
            if 0<=nx<N and 0<=ny<M and board[nx][ny]!=0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    board[nx][ny] = cur + 1
                    q.append((nx, ny))
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] != 0:
                board[i][j] = -1
    
    for row in board:
        print(*row)

if __name__ == "__main__":
    solution()
