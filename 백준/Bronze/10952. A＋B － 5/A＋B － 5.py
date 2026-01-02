import sys

input = sys.stdin.readline


def solution():
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        print(A + B)


if __name__ == "__main__":
    solution()
