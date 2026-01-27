import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    cards = list(map(int, input().split()))

    count = {}
    for num in cards:
        if num in count.keys():
            count[num] += 1
        else:
            count[num] = 1
    
    M = int(input())
    q = list(map(int, input().split()))

    ans = []
    for num in q:
        if num in count.keys():
            ans.append(count[num])
        else:
            ans.append(0)
    
    print(*ans)

if __name__ == "__main__":
    solution()
