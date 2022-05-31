# 문제 : N과M (2)
# 제출일 : 2022.05.31 (12:30)
'''
자연수 N과 M이 주어졌을 때, 
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1. 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
2. 고른 수열은 오름차순이어야 한다.
'''

# 내 풀이
from itertools import combinations

n, m = map(int, input().split())
b = [str(ms) for ms in range(1,n+1)]
c = list(map(' '.join, combinations(b, m)))
for i in range(len(c)):
    print(c[i])

# 모범 답안
n, m = map(int, input().split())
def f(v,nn,mm):
 if mm>=m:
  print(v[:len(v)-1])
  return
 for i in range(nn,n+1):
  if v.count(str(i))==0:
   mm+=1
   t=v+str(i)+' '
   f(t,i,mm)
   mm-=1
f('',1,0)