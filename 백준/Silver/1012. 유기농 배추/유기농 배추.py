import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

def solution():
    T = int(input())

    ## field state ## 
    # 0: 배추도 없고 지렁이가 움직일수도 없음
    # 1: 벌레가 미방문한 배추
    # 2: 벌레가 방문한 배추

    def DFS(field: list):
        # 필요한 배추흰지렁이 숫자
        ans = 0
        col_limit = len(field)-1 # which is M-1
        row_limit = len(field[0])-1 # which is N-1


        def DFS_visit(x, y):
            # 벌레 방문
            field[x][y] = 2
            # 인접 배추 확인 및 방문
            for i in range(4): # 동서북남
                nx, ny = x + DX[i], y + DY[i]
                # 범위 체크
                if 0 <= nx <= col_limit and 0 <= ny <= row_limit:
                    # next가 미방문 배추면 새로 방문
                    if field[nx][ny] == 1:
                        DFS_visit(nx, ny)
        
        for sx in range(col_limit+1): # 0부터 M-1
            for sy in range(row_limit+1): # 0부터 N-1
                if field[sx][sy] == 1: # 배추가 있고 미방문이면
                    ans += 1
                    DFS_visit(sx, sy)

        return ans

    for _ in range(T):
        M, N, K = map(int, input().split())

        # 0으로 초기화된 M x N 행렬 만들기
        field = [[0 for _ in range(N)] for _ in range(M)]

        # 배추가 심어진걸 1로 표시        
        for _ in range(K):
            x, y = map(int, input().split())
            field[x][y] = 1

        ans = DFS(field)

        print(ans)

if __name__ == "__main__":
    solution()
