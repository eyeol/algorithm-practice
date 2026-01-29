import sys

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    
    ddmh = []
    bdmh = []

    for _ in range(N):
        ddmh.append(input().strip())

    for _ in range(M):
        bdmh.append(input().strip())

    ans = list(set(ddmh)&set(bdmh))

    ans.sort()

    print(len(ans))
    for name in ans:
        print(name)

if __name__ == "__main__":
    solution()
