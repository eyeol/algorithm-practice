import sys

input = sys.stdin.readline


def solution():

    def determine_Palindrome(x: str):
        N = len(x)
        for i in range(N // 2):
            if x[i] != x[-1 - i]:  # 맨 앞과 맨 뒤부터 비교 시작
                return False  # 다른걸 찾으면 early return
        # 위에서 return되지 않았다면 비교한 값이 모두 같은 것
        return True

    while True:
        num = input().strip()
        if num == "0":
            break
        if determine_Palindrome(num):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    solution()
