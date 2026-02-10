import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    if N >= K:
        print(N - K)
        return

    MAX = 100000  
    dist = [-1] * (MAX + 1)
    q = deque([N])
    dist[N] = 0

    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            return

        nx = x - 1
        if nx >= 0 and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

        nx = x + 1
        if nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

        nx = x * 2
        if nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

if __name__ == "__main__":
    solution()
