import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    X = list(map(int, input().split()))

    sorted_X = sorted(list(set(X)))

    index = {}
    for i, x in enumerate(sorted_X):
        index[x] = i # 작은 녀석부터 인덱스 기록(몇번째로 작은지)
    
    pre = [0]*len(sorted_X)
    for i in range(1, len(pre)):
        pre[i] = pre[i-1] + 1 # 누적합 방식으로 자기보다 작은 좌표의 개수 기록

    ans = []
    for x in X:
        i = index[x]
        ans.append(pre[i])
    
    print(*ans)


if __name__ == "__main__":
    solution()
