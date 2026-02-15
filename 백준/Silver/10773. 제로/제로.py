import sys

input = sys.stdin.readline

def solution():
    K = int(input())
    book = []
    for _ in range(K):
        call = int(input())
        if call == 0:
            book.pop()
        else:
            book.append(call)
    
    print(sum(book))

if __name__ == "__main__":
    solution()