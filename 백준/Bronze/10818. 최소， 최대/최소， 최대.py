import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[0], nums[-1])


if __name__ == "__main__":
    solution()
