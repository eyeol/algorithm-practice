import sys

input = sys.stdin.readline


def solution():

    N = int(input())
    gts = set(list(map(int, input().split())))

    M = int(input())
    nums = list(map(int, input().split()))

    for num in nums:
        print(1 if num in gts else 0)


if __name__ == "__main__":
    solution()
