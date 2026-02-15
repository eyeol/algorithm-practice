import sys

input = sys.stdin.readline

# push하는 순서는 반드시 오름차순
# 임의의 수열이 주어졌을 때, 스택으로 그 수열 만들 수 있는지
# 있다면 어떤 순서로 push, pop해야 하는지

def solution():
    N = int(input())
    
    # 스택
    stack = []
    # 스택에 들어갈 숫자 따로 관리
    nxt = 1
    
    # push, pop 순서 기록
    ans = []

    for _ in range(N):
        # 스택에서 반환해야 하는 수
        num = int(input())

        # stack이 비어있다면
        # 가능/불가능 먼저 판단
        # 가능하면 얼마나 넣을지
        # 넣고 빼야 함
        if not stack:
            # 다음에 넣을값이 num보다 같거나 작다면 가능
            if nxt <= num:
                # 채우기
                while nxt<=num:
                    stack.append(nxt)
                    ans.append("+")
                    nxt += 1
                # 그 다음 num과 같은 숫자 빼기
                stack.pop()
                ans.append("-")
            else: # nxt > num이면 불가능
                print("NO")
                return
        else: #스택이 이미 있다면
            # top이랑 num이 같다면
            if stack[-1]==num:
                stack.pop()
                ans.append("-")
            else: # top이랑 num이 다름
                if nxt <= num:
                    while nxt<=num:
                        stack.append(nxt)
                        ans.append("+")
                        nxt += 1
                    stack.pop()
                    ans.append("-")
                else:
                    print("NO")
                    return
    
    for op in ans:
        print(op)


if __name__ == "__main__":
    solution()