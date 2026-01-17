import sys
from collections import deque

input = sys.stdin.readline


def solution():

    N = int(input())

    q = deque([])

    for _ in range(N):
        inst = list(input().split())
        if inst[0] == "push":
            q.append(int(inst[1]))
        elif inst[0] == "pop":
            if q:
                print(q.popleft())
            else:  # stack is empty
                print(-1)
        elif inst[0] == "size":
            print(len(q))
        elif inst[0] == "empty":
            if q:
                print(0)
            else:
                print(1)
        elif inst[0] == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        elif inst[0] == "back":
            if q:
                print(q[-1])
            else:
                print(-1)


if __name__ == "__main__":
    solution()
