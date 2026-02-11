import sys

input = sys.stdin.readline

# greedy algorithm

def solution():
    N = int(input())
    table = []

    for _ in range(N):
        s, e = map(int, input().split())
        table.append((s, e))

    table.sort(key=lambda x: (x[1], x[0]))

    ans = 1
    last = table[0][1]

    for i in range(1, N): # 1부터 N-1 ; N-1개 탐색
        # 회의 시작 시간이 last보다 크거나 같으면
        if table[i][0] >= last:
            last = table[i][1]
            ans += 1

    print(ans)

if __name__ == "__main__":
    solution()