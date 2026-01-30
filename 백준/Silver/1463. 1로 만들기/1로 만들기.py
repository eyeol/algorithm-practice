import sys

input = sys.stdin.readline

# dp table 만들어야 하는듯한 느낌

def solution():
    N = int(input())
    
    dp = [0] * (N + 1)

    for i in range(2, N+1):
        v = dp[i-1] + 1
        if i % 2 == 0:
            t = dp[i//2] + 1
            if t < v:
                v = t
        if i % 3 == 0:
            t = dp[i//3] + 1
            if t < v:
                v = t
        dp[i] = v
    
    print(dp[N])

if __name__ == "__main__":
    solution()
