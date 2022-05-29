# 문제 : N과 M(1)
# 제출일 : 2022.05.30 (09:00)
'''
자연수 N과 M이 주어졌을 때,
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

# 내 풀이
from itertools import permutations

n, m = map(int, input().split())
b = [str(ms) for ms in range(1,n+1)]
c = list(map(' '.join, permutations(b, m)))
for i in range(len(c)):
    print(c[i])

# 모범 답안
from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join,permutations(li, M)))))