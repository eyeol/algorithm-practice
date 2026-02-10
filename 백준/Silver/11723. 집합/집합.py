import sys

input = sys.stdin.readline

def solution():
    M = int(input())
    S =set([])
    for _ in range(M):
        command = list(input().split())
        if command[0] == "all":
            S = set(range(1, 21))
        if command[0] == "empty":
            S = set([])
        if command[0] == "add":
            S.add(int(command[1]))
        if command[0] == "remove":
            S.discard(int(command[1]))
        if command[0] == "check":
            if int(command[1]) in S:
                print(1)
            else:
                print(0)
        if command[0] == "toggle":
            if int(command[1]) in S:
                S.discard(int(command[1]))
            else:
                S.add(int(command[1]))


if __name__ == "__main__":
    solution()
