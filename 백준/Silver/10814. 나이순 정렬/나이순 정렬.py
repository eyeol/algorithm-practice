import sys

input = sys.stdin.readline


def solution():

    N = int(input())

    members = []
    for _ in range(N):
        age, name = input().split()
        members.append((int(age), name))

    members.sort(key=lambda x: (x[0]))

    for member in members:
        print(member[0], member[1])


if __name__ == "__main__":
    solution()
