import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    pairs = []

    for _ in range(N):
        x, y = map(int, input().split())
        pairs.append((x, y))

    pairs.sort(key=lambda x:(x[0], x[1]))
    for p in pairs:
        print(p[0], p[1])

if __name__ == "__main__":
    solution()
