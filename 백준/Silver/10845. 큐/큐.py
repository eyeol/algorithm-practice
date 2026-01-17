import sys
from collections import deque

input = sys.stdin.readline


def solution():

    N = int(input())

    q = deque([])
    out = []

    for _ in range(N):
        inst = list(input().split())
        if inst[0] == "push":
            q.append(int(inst[1]))
        elif inst[0] == "pop":
            out.append(str(q.popleft() if q else "-1"))
        elif inst[0] == "size":
            out.append(str(len(q)))
        elif inst[0] == "empty":
            out.append("0" if q else "1")
        elif inst[0] == "front":
            out.append(str(q[0]) if q else "-1")
        elif inst[0] == "back":
            out.append(str(q[-1]) if q else "-1")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solution()
