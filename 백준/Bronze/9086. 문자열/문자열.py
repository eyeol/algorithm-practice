import sys

input = sys.stdin.readline

def solution():
    T = int(input())

    for _ in range(T):
        word = input().strip()
        ans = word[0] + word[-1]
        print(ans)

if __name__ == "__main__":
    solution()