import sys

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    
    name_dict = {}

    for _ in range(N):
        name = input().strip()
        name_dict[name] = 1

    for _ in range(M):
        name = input().strip()
        if name in name_dict.keys():
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    ans = 0
    ans_names = []
    for name in name_dict.keys():
        if name_dict[name] == 2:
            ans += 1
            ans_names.append(name)
    ans_names.sort()

    print(ans)
    for name in ans_names:
        print(name)

if __name__ == "__main__":
    solution()
