import sys

input = sys.stdin.readline

# dp table 만들어야 하는듯한 느낌

def solution():
    N = int(input())
    
    dp = [(N, 0)]

    i = 0
    while dp[i][0] > 1:
        num = dp[i][0]
        curr = dp[i][1]
        if num % 3 == 0:
            dp.append((num//3, curr+1))
        if num % 2 == 0:
            dp.append((num//2, curr+1))
        dp.append((num-1, curr+1))
        i += 1
    
    print(dp[i][1])

if __name__ == "__main__":
    solution()
