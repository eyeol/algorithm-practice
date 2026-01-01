import sys

input = sys.stdin.readline


def solution():
    A, B = map(int, input().split())
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:  # A == B
        print("==")


if __name__ == "__main__":
    solution()
