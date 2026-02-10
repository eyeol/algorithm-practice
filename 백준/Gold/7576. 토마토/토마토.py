import sys
from collections import deque

input= sys.stdin.readline

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

def solution():
    M, N = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    riped = []
    for i in range(N): # row ; x
        for j in range(M): # col ; y
            if board[i][j] == 1:
                riped.append((i, j, 0))

    q = deque(riped)
    ans = 0
    
    while q:
        cx, cy, t = q.popleft()
        ans = max(ans, t)
        for i in range(4):
            nx, ny = cx+DX[i], cy+DY[i]
            # 범위 확인
            if 0<=nx<=N-1 and 0<=ny<=M-1:
                # 익지 않은 토마토인지 확인
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    q.append((nx, ny, t+1))
    
    not_riped = 0
    for b in board:
        if 0 in b:
            not_riped = 1

    if not_riped:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    solution()
