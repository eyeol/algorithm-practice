import sys

input = sys.stdin.readline


def solution():
    A, B = map(int, input().split())
    print(A+B)


if __name__ == "__main__":
    solution()