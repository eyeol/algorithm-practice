import sys

input = sys.stdin.readline


def solution():

    def determine_right(a, b, c):
        a2 = a**2
        b2 = b**2
        c2 = c**2

        if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
            return True
        else:
            return False

    while True:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break
        if determine_right(a, b, c):
            print("right")
        else:
            print("wrong")


if __name__ == "__main__":
    solution()
