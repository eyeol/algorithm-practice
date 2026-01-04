import sys

input = sys.stdin.readline

# Given
# 체스판의 조건: 흰백(WB) 번갈아서 칠해져야 함

# Goal
# 지민이가 필요한건 8x8 크기의 체스판
# 지민이가 칠해야 하는 정사각형의 최소 개수

# How to solve
# 정답 보드를 미리 세팅; 두 종류(흰으로 시작 / 백으로 시작)
# 모든 케이스에 대해 오차를 측정해서 최소값을 기록
# M=10이면 탐색할 세로 인덱스는 0, 1, 2=M-8 ; 3개
# N=13이면 탐색할 가로 인덱스는 0, 1, ... , 5=N-8 ; 6개


# 정답 보드 세팅
board_1 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

board_2 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]


def solution():
    M, N = map(int, input().split())
    board = [input().strip() for _ in range(M)]

    # 이론상 최대치로 정답 초기화
    ans = 64

    def measure_diff(x: int, y: int):
        sum_1 = 0
        sum_2 = 0
        for i in range(8):  # 0 to 7
            for j in range(8):  # 0 to 7
                if board[x + i][y + j] != board_1[i][j]:
                    sum_1 += 1
                if board[x + i][y + j] != board_2[i][j]:
                    sum_2 += 1
        return min(sum_1, sum_2)

    for i in range(M - 7):
        for j in range(N - 7):
            # 8x8 사이즈를 잘라서 보드 2개와 비교
            candidate = measure_diff(i, j)
            ans = min(candidate, ans)

    print(ans)


if __name__ == "__main__":
    solution()
