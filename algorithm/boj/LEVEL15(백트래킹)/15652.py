# 문제 : N과 M (4)
# 제출일 : 2022.06.02 (13:30)
'''
자연수 N과 M이 주어졌을 때, 
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1. 1부터 N까지 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 된다.
3. 고른 수열은 비내림차순이어야 한다.
4. 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
'''

# 내 풀이 - (메모리 초과)
from itertools import product

n, m = map(int, input().split())
b = [str(ms) for ms in range(1,n+1)]
c = list(map(''.join, product(b, repeat = m)))
d = []
for i in range(len(c)):
    d += [list(c[i])]
    d[i].sort()

result = []
for value in d:
    if value not in result:
        result.append(value)
        
for j in range(len(result)):
    print(' '.join(result[j]))

# 모범 답안
n,m = map(int, input().split())
 
s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1)
