import sys

input = sys.stdin.readline

# DFS의 Nesting intervals property를 이용하면 될듯
# stack을 쓰자


def solution():
    T = int(input())


    # 괄호 인풋을 그래프 탐색으로 생각하면 됨
    def is_Valid(ps: str):
        
        stack = 0

        # ( ; White -> Gray
        # ) ; Gray -> Black

        # VPS를 위한 규칙
        # White -> Gray 후에 Black으로 칠하면서 마무리해야 함
        # White -> Gray 없이 )가 먼저 나오는 것
        for ch in ps:
            if ch == "(":
                stack += 1
            else: # ch = ")"
                if stack == 0: # 스택이 비어있는데 Black으로 칠하는 상황
                    return False
                else: # stack is not empty
                    stack -= 1
        
        if stack > 0: # 모든 인풋 받은 후에 스택에 잔여 원소가 있으면 not Valid
            return False

        return True

    for _ in range(T):
        ps = input().strip()
        if is_Valid(ps):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solution()
