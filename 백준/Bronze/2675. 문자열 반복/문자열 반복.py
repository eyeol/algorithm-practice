import sys

input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        repeat, word = input().split()
        repeat = int(repeat)

        new_word = ""
        for ch in word:
            new_word += ch * repeat

        print(new_word)


if __name__ == "__main__":
    solution()
