import sys
from collections import deque

input = sys.stdin.readline

# parametric search였나 그랬던거 같다

def solution():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    max_height = max(trees)

    def get_tree(trees: list, h: int): # 시간복잡도 = 100만
        added = 0
        for tree in trees:
            if tree > h:
                added += tree - h

        return added
    
    def get_h(u, b):
        return((u+b)//2)
    

    u = max_height
    b = 0
    pre = -1

    while True:
        h = get_h(u, b)
        if h == pre:
            break
        pre = h
        result = get_tree(trees, h)
        if result == M:
            break
        elif result < M: # 나무가 부족하다 -> h 낮춰야 한다
            u = h
        elif result > M: # 나무가 많다 -> h 높여도 된다
            b = h
    print(h)


if __name__ == "__main__":
    solution()
