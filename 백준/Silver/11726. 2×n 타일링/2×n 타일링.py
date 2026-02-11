import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    if N < 2:
        print(1)
    elif N == 2:
        print(2)
    else:
        dp = [0]*(N+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, N+1): # 3부터 N까지
            dp[i] = dp[i-2] + dp[i-1]
        
        print(dp[N]%10007)

if __name__ == "__main__":
    solution()
