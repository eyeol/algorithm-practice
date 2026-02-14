import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    
    # 길이 최대 1001
    # 0부터 upper bound까지 upper bound+1개
    candidate = list(range(0, N//5+1))

    ans = []
    # 5kg 봉지 개수마다 확인
    for num in candidate:
        # 5kg 봉지로 담고 남은 설탕 무게
        remain = N - 5*num
        if remain == 0: # 나누어떨어지면 그게 최소 개수
            print(num)
            return
        else: # 안나누어떨어지면
            # 3으로 나누어떨어지는지 확인
            if remain%3 == 0:
                # 나누어떨어지면
                num2 = remain//3
                ans.append(num+num2)
    
    if ans:
        print(min(ans))
    else:
        print(-1)

if __name__ == "__main__":
    solution()