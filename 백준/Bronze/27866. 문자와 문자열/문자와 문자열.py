import sys
from collections import deque

input = sys.stdin.readline


def solution():
    S = input().strip()
    i = int(input())

    print(S[i - 1])


if __name__ == "__main__":
    solution()
