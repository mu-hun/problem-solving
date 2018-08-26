#-*- coding: utf-8 -*-
# 아래 solve 함수를 작성하세요.
# 올바른 덱인지 여부에 따라 "valid", "invalid"를 리턴하세요.

# N: 카드의 수
# resources: 카드별 요구하는 자원의 배열

def solve(N, resources):
    sample_resource = ['gold', 'mana', 'light', 'dark', 'nature']
    property_list = [0, 0, 0, 0, 0]
    if N > 12:
        return "invalid"
    for i in resources:
        property_list[sample_resource.index(i)] += 1
    if len(filter(lambda x: if x > 0)) < 4:
        return "valid"
    else:
        return "invalid"
    
N = int(input())                                 # stub
resources = [input() for y in range(N)]             # stub

ret = solve(N, resources)                  # stub
print(ret) # stub
