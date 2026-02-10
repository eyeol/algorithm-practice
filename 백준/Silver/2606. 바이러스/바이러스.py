import sys
from collections import deque

input = sys.stdin.readline


def solution():
    V = int(input())
    N = int(input())

    adj = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    # edge 개수
    for _ in range(N):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    ans = 0
    q = deque([1])
    visited[1] = True

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = 1
                ans += 1
                q.append(v)
    
    print(ans)



if __name__ == "__main__":
    solution()
