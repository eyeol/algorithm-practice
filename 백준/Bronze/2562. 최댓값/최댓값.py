import sys

input = sys.stdin.readline


def solution():
    nums = []
    for i in range(1, 10):  # 1부터 9
        nums.append((int(input()), i))

    nums.sort(key=lambda x: x[0])
    maximum = nums[-1]
    
    print(maximum[0])
    print(maximum[1])


if __name__ == "__main__":
    solution()
