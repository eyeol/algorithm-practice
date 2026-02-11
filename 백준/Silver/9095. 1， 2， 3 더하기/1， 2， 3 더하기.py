import sys

input= sys.stdin.readline


def solution():
    T = int(input())

    pre = [0]*11
    pre[1] = 1
    pre[2] = 2
    pre[3] = 4

    for i in range(4, 11):
        pre[i] = pre[i-1] + pre[i-2] + pre[i-3]

    for _ in range(T):
        num = int(input())
        print(pre[num])


if __name__ == "__main__":
    solution()
