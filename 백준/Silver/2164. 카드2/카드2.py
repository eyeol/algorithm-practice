import sys

from collections import deque


def solution():

    N = int(sys.stdin.readline())
    deq = deque(range(1, N + 1))

    while deq:
        discard = deq.popleft()
        # 꺼냈는데 deq이 비어있다 = 마지막 카드다
        if not deq:
            print(discard)
            return
        moved = deq.popleft()
        if not deq:
            print(moved)
            return
        deq.append(moved)


if __name__ == "__main__":
    solution()
