import sys

input = sys.stdin.readline


def solution():
    while True:
        nums = input()
        if not nums:
            break
        A, B = map(int, nums.split())
        print(A + B)


if __name__ == "__main__":
    solution()
