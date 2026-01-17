import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    stack = []
    out = []

    for _ in range(N):
        inst = input().split()
        if inst[0] == "push":
            stack.append(int(inst[1]))
        elif inst[0] == "pop":
            out.append(str(stack.pop()) if stack else "-1")
        elif inst[0] == "size":
            out.append(str(len(stack)))
        elif inst[0] == "empty":
            out.append("0" if stack else "1")
        else:  # top
            out.append(str(stack[-1]) if stack else "-1")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solution()
