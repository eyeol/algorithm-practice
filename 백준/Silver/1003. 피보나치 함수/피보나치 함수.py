import sys

input = sys.stdin.readline


def solution():
    T = int(input())

    def record_counts(n: int):
        if n == 0:
            return 1, 0
        elif n == 1:
            return 0, 1
        # 0부터 n까지
        # (x, y) ; x가 0 호출 수, y가 1 호출 수
        counts = [[0, 0] for _ in range(n+1)]
        counts[0] = [1, 0]
        counts[1] = [0, 1]

        for i in range(2, n+1): # 2부터 n까지
            counts[i][0] = counts[i-2][0] + counts[i-1][0]
            counts[i][1] = counts[i-2][1] + counts[i-1][1]
        
        return counts[-1]

    for _ in range(T):
        num = int(input())
        ans = record_counts(num)

        print(ans[0], ans[1])
        
if __name__ == "__main__":
    solution()
