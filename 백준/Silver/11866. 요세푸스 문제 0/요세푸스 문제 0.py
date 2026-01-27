import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    q = deque(range(1, N+1))

    ans = []
    while q: # 모두 제거될 때까지
        for i in range(K-1): # 앞에 K-1개는 뒤로 치우기
            out = q.popleft()
            q.append(out)
        # K번째는 진짜 제거해서 ans에 넣기
        ans.append(str(q.popleft()))
    
    ans_str = ", ".join(ans)
    print("<" + ans_str + ">")

if __name__ == "__main__":
    solution()
