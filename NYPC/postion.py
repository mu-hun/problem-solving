#-*- coding: utf-8 -*-
# 아래 solve 함수를 작성하세요.
# 캐릭터가 갖게 될 체력을 리턴하세요.

# A : 현재 체력
# B : 최대 체력
# H : 마실 포션의 회복량

def solve(A, B, H):
    sum_one, b_per_150 = A + H, int(B * 150 / 100)
    if sum_one < B:
        return sum_one
    elif sum_one < b_per_150:
        add_25_per = int((sum_one - B) * 25 / 100) + B
        return add_25_per
    else:
        return b_per_150

A, B, H = [int(x) for x in input().split()]

print(solve(A, B, H))
