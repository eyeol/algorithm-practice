import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    scores = list(map(int, input().split()))
    maximum = max(scores)

    ans = (sum(scores) / maximum) * (100 / N)
    print(ans)


if __name__ == "__main__":
    solution()
