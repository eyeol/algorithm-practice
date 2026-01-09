import sys

input = sys.stdin.readline

# 각 숫자의 소인수분해 멤버를 A와 B라고 할 때
# 최대공약수 = A intersection B
# 최소공배수 = A union B


def solution():

    num_1, num_2 = map(int, input().split())

    # 소인수분해
    def Prime_Factorize(num: int):
        primes = []

        i = 2
        while num != 1:
            # 나누어떨어지면
            if num % i == 0:
                primes.append(i)
                num = num // i
                i = 1
            i += 1
        # 소인수분해 결과를 return
        return primes

    # set으로 만들면 안됨
    A = Prime_Factorize(num_1)
    B = Prime_Factorize(num_2)

    # 차집합 구하기
    A_minus_B = list(A)
    for prime in B:
        if prime in A_minus_B:
            A_minus_B.remove(prime)

    B_minus_A = list(B)
    for prime in A:
        if prime in B_minus_A:
            B_minus_A.remove(prime)

    inter = list(A)
    for prime in A_minus_B:
        if prime in inter:
            inter.remove(prime)

    def get_answer(arr: list):
        ans = 1
        for num in arr:
            ans *= num
        return ans

    ans_1 = get_answer(inter)
    ans_2 = ans_1 * get_answer(A_minus_B) * get_answer(B_minus_A)

    print(ans_1)
    print(ans_2)


if __name__ == "__main__":
    solution()
