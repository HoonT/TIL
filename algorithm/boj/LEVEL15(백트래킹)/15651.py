# 문제 : N과M (3)
# 제출일 : 2022.. (:)
'''
자연수 N과 M이 주어졌을 때,
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1. 1부터 N까지 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 된다.
'''

# 내 풀이
from itertools import product

n, m = map(int, input().split())
b = [str(ms) for ms in range(1,n+1)]
c = list(map(' '.join, product(b, repeat = m)))
for i in range(len(c)):
    print(c[i])

# 모범 답안
from itertools import product
n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
print('\n'.join(list(map(' '.join,product(map(str,arr),repeat=m)))))