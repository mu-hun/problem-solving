#-*- coding: utf-8 -*-
# 아래 solve 함수를 작성하세요.
# 올바른 덱인지 여부에 따라 "valid", "invalid"를 리턴하세요.

# N: 카드의 수
# resources: 카드별 요구하는 자원의 배열

def solve(N, resources):
    resource = ['gold', 'mana', 'light', 'dark', 'nature']
    sock_sung_list = [0, 0, 0, 0, 0]
    sock_num = 0
    if N > 12:
        return "invalid"
    for i in resources:
        resource_location = resource.index(i)
        sock_sung_list[resource_location] += 1
    for sock_sung in sock_sung_list:
        if not sock_sung == 0:
            sock_num += 1
    if sock_num < 4:
        return "valid"
    else:
        return "invalid"

N = int(input())                                 # stub
resources = [input() for y in range(N)]             # stub

ret = solve(N, resources)                  # stub
print(ret) # stub
