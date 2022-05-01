# 문제 : 블랙잭
# 제출일 : 2022.. (:)
'''
N장의 카드에 써져 있는 숫자가 주어졌을 때, 
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
'''

# 내 풀이
import itertools

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
result = list(itertools.combinations(b,3))
for i in range(len(result)):
    if sum(result[i]) <= a[1]:
        c += [sum(result[i])]

print(max(c))

# 모범 답안
