import sys


def solution():

    _, *nums = map(int, sys.stdin.buffer.read().split())

    def determine_prime(x: int):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        i = 3
        while i * i <= x:  # 제곱근까지 확인
            if x % i == 0:
                return False
            i += 2  # 홀수만 확인
        return True

    ans = 0
    for num in nums:
        if determine_prime(num):
            ans += 1

    print(ans)


if __name__ == "__main__":
    solution()
