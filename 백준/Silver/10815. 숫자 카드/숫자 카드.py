import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    yesno = list(map(int, input().split()))

    table = {}
    for num in cards:
        table[num] = 1

    for num in yesno:
        if num in table:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solution()