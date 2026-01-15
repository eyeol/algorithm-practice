import sys

input = sys.stdin.readline


def solution():

    N = int(input())
    sizes = list(map(int, input().split()))
    T, P = map(int, input().split())

    t_bundles = 0
    for size in sizes:
        t_bundles += (size // T) + 1
        if size % T == 0:   
            t_bundles -= 1  # 나누어떨어지면 -1

    p_bundles = N // P
    p_indiv = N % P

    print(t_bundles)
    print(p_bundles, p_indiv)


if __name__ == "__main__":
    solution()
