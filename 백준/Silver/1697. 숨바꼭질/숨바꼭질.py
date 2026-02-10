import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())

    if N >= K:
        print(N-K)
    else: # N < K
        # BFS로..?
        time = [1000000]*(K*2+1) # 0부터 2K까지
        time[N] = 0
        
        def bfs(time: list, s: int):
            q = deque([s])
            
            while q:
                u = q.popleft()
                next = [u-1, u+1, 2*u]
                for index in next:
                    if 0 <= index <= 2*K:
                        if time[u]+1 < time[index]:
                            time[index] = time[u] + 1
                            if index == K:
                                print(time[index])
                                return
                            q.append(index)
        
        bfs(time, N)


if __name__ == "__main__":
    solution()
