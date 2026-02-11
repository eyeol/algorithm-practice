import sys

input= sys.stdin.readline


def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # determine to cut
    def d2c(sx: int, sy: int, side: int):
        color = board[sx][sy]
        b = 0
        w = 0

        if side == 1:
            if color: # 파랑색 종이
                b += 1
            else:     # 하얀색 종이
                w += 1
            return b, w
        
        cut = 0
        for i in range(sx, sx+side):
            for j in range(sy, sy+side):
                # 대표 색과 다르면 자르기
                if board[i][j] != color:
                    cut = 1
        
        if not cut:
            if color:
                b += 1
            else:
                w += 1
        else: # cut
            side = side // 2
            b1, w1 = d2c(sx, sy, side)
            b2, w2 = d2c(sx, sy+side, side)
            b3, w3 = d2c(sx+side, sy, side)
            b4, w4 = d2c(sx+side, sy+side, side)
            b = b1 + b2 + b3 + b4
            w = w1 + w2 + w3 + w4
        
        return b, w

    sx = 0
    sy = 0
    side = N    
    b, w = d2c(sx, sy, side)
    print(w)
    print(b)



if __name__ == "__main__":
    solution()
