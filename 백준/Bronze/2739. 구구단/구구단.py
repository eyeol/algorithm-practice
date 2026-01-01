import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    for i in range(1, 10):  # 1부터 9
        print(f"{N} * {i} = {N*i}")


if __name__ == "__main__":
    solution()
