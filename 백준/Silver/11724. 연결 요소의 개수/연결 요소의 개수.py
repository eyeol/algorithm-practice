import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # bfs
    def bfs(s: int):
        visited[s] = 1
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
    
    ans = 0
    for vertex in range(1, N+1): # 1부터 N
        if not visited[vertex]:
            ans += 1
            bfs(vertex)

    print(ans)

if __name__ == "__main__":
    solution()
