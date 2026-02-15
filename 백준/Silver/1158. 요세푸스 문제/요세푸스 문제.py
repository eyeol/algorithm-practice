import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    q = deque(range(1, N+1)) # 1부터 N

    result = []
    while q:
        for _ in range(K-1): # K-1번 뒤로 보내기
            tmp = q.popleft()
            q.append(tmp)
        num = q.popleft()
        result.append(str(num))
    
    ans = "<" + ", ".join(result) + ">"
    print(ans)


if __name__ == "__main__":
    solution()