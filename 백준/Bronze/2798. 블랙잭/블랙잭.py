import sys

from itertools import combinations

# 카드의 합이 M을 넘지 않는 한도 내에서 카드 합 최대로


def solution():

    N, M, *cards = map(int, sys.stdin.buffer.read().split())

    ans = 0
    for comb in combinations(cards, 3):
        candidate = sum(comb)

        if candidate <= M and candidate > ans:
            ans = candidate

    print(ans)


if __name__ == "__main__":
    solution()
