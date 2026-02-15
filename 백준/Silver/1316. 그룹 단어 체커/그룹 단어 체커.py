import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    def group_check(word: str):
        seen = []
        cur = " "
        for ch in word:
            if ch not in seen:
                seen.append(ch)
                cur = ch
            else: # 이미 봤는데 cur가 아니면
                if ch != cur:
                    return False
        return True

    words = []
    for _ in range(N):
        words.append(input().strip())
    
    ans = 0
    for word in words:
        if group_check(word):
            ans += 1

    print(ans)


if __name__ == "__main__":
    solution()