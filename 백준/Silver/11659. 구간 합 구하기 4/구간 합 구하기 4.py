import sys

input = sys.stdin.readline

# 구간합 문제

def solution():
    N, M = map(int, input().split())

    nums = [0] + list(map(int, input().split()))
    prefix = [0] * (N+1)
    prefix[1] = nums[1]
    for i in range(1, N+1): # 1부터 N까지
        prefix[i] = prefix[i-1] + nums[i]

    for _ in range(M):
        i, j = map(int, input().split())
        print(prefix[j] - prefix[i-1])

if __name__ == "__main__":
    solution()
