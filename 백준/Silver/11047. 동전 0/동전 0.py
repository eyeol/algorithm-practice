import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())

    coins = []
    for _ in range(N):
        coins.append(int(input()))
    
    i = -1
    ans = 0

    while K > 0:
        cur = coins[i]
        if K >= cur:
            ans += K//cur
            K = K%cur
        i -= 1
    
    print(ans)


if __name__ == "__main__":
    solution()