import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    def dc(r, c, n):
        color = board[r][c]
        same = True
        for i in range(r, r+n):
            for j in range(c, c+n):
                if board[i][j] != color:
                    same = False
                    break
            if not same:
                break

        if same:
            if color == 1:
                return 1, 0   # (blue, white)
            else:
                return 0, 1

        half = n // 2
        b1, w1 = dc(r, c, half)
        b2, w2 = dc(r, c+half, half)
        b3, w3 = dc(r+half, c, half)
        b4, w4 = dc(r+half, c+half, half)
        return (b1+b2+b3+b4, w1+w2+w3+w4)

    b, w = dc(0, 0, N)
    print(w)
    print(b)

if __name__ == "__main__":
    solution()
