import sys

input = sys.stdin.readline

# 모든 보드를 전부 메모리에 올릴 수 없음
# 메모리에 올릴 보드를 재귀적으로 찾으면 됨

# 처음엔 전체의 1/4 중에서 찾기
# 그 다음엔 그 1/4 중에서 1/4 영역 찾기
# 범위의 넓이가 1이 될 때까지 반복

def solution():
    N, r, c = map(int, input().split())
    sx, sy, ex, ey = 0, 0, 2**N, 2**N
    box = (sx, sy, ex, ey)
    ans = 0

    def which_quadrant(box: tuple, r: int, c: int, ans):
        # row/col start, row/col end  unpacking
        rs, cs, re, ce = box
        
        # 유닛은 절대 길이 기반
        diff = (re - rs) // 2
        unit = diff*diff

        
        rm = (rs + re) // 2
        cm = (cs + ce) // 2

        # quartify row range
        if rs <= r < rm:
            re = rm
        else: # rm <= r < re
            rs = rm
            ans += 2*unit

        # quartify col range
        if cs <= c < cm:
            ce = cm
        else: # cm <= c < ce
            cs = cm
            ans += unit
        # 1사분면은 ans + 1 unit
        # 2사분면은 그대로
        # 3사분면은 ans + 2 unit
        # 4사분면은 ans + 3 unit
        return (rs, cs, re, ce), ans
    
    # 사각형 한 변이 1보다 클 동안 반복
    while ex - sx > 1:
        new_box, new_ans = which_quadrant(box, r, c, ans)
        sx, sy, ex, ey = new_box
        box = (sx, sy, ex, ey)
        ans = new_ans
    
    print(new_ans)

if __name__ == "__main__":
    solution()
