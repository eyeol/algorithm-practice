import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N = int(input())

    num = input().strip()
    sum = 0
    for i in range(N):
        sum += int(num[i])

    print(sum)


if __name__ == "__main__":
    solution()
