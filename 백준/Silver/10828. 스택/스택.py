import sys

input = sys.stdin.readline


def solution():

    N = int(input())

    stack = []
    for _ in range(N):
        inst = list(input().split())
        if inst[0] == "push":
            stack.append(int(inst[1]))
        elif inst[0] == "pop":
            if stack:
                print(stack.pop(-1))
            else:  # stack is empty
                print(-1)
        elif inst[0] == "size":
            print(len(stack))
        elif inst[0] == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif inst[0] == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)


if __name__ == "__main__":
    solution()
