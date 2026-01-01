import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    for i in range(1, N + 1):  # 1부터 N
        out = "*" * i
        print(out)


if __name__ == "__main__":
    solution()
