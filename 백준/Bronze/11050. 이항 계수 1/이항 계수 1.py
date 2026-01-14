import sys

input = sys.stdin.readline


def solution():

    N, K = map(int, input().split())

    numer, denom = 1, 1

    for i in range(1, K + 1):  # 1부터 K
        denom *= i

    for i in range(N, N - K, -1):  # N부터 N-K+1
        numer *= i

    ans = numer // denom
    print(ans)


if __name__ == "__main__":
    solution()
