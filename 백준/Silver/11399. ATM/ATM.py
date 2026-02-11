import sys


def solution():
    N, *p = map(int, sys.stdin.buffer.read().split())
    p.sort()

    pre = [0]*N
    pre[0] = p[0]
    for i in range(1, N): # 0부터 N-1
        pre[i] = p[i] + pre[i-1]
    
    print(sum(pre))

if __name__ == "__main__":
    solution()
