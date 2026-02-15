import sys

input = sys.stdin.readline


def solution():
    exp = input().strip()

    # 연산자 위치와 연산자 종류를 기록해야 함
    operator = []
    # 피연산자도 따로 기록하자
    operand = ""

    for i in range(len(exp)):
        if exp[i] =="+" or exp[i] == "-":
            operator.append(exp[i])
            operand += " "
        else:
            operand += exp[i]

    nums = list(map(int, operand.split()))

    # 결과를 최소로 만드는게 목적
    # 뒤에서부터 +은 더하고 -은 누적값을 빼면 됨
    
    # 누적값
    ans = 0
    # -가 나올때까지 임시로 합하는 값
    tmp = 0

    i = len(nums) - 1

    # 마지막 숫자를 tmp에 미리 넣음
    tmp += nums[i]

    i -= 1    
    while i >= 0: # len(nums)-2부터 0까지; 연산자 수만큼 반복
        if operator[i] == "+":
            tmp += nums[i]
        else: # operand[i] == "-"
            ans -= tmp
            tmp = int(nums[i])
        i -= 1
    
    ans += tmp
    print(ans)


if __name__ == "__main__":
    solution()