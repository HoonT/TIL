# 문제 : 검문
# 제출일 : 2022.05.16 (19:00)
'''
먼저 근처에 보이는 숫자 N개를 종이에 적는다. 
그 다음, 종이에 적은 수를 M으로 나누었을 때, 
나머지가 모두 같게 되는 M을 모두 찾으려고 한다. 
M은 1보다 커야 한다.

N개의 수가 주어졌을 때, 가능한 M을 모
두 찾는 프로그램을 작성하시오.
'''

# 내 풀이
import math

N=int(input())
a=[]
b=[]
g=0
for i in range(N):
    a.append(int(input()))
    if i==1:
        g=abs(a[1]-a[0])
    g=math.gcd(abs(a[i]-a[i-1]), g)
gf=int(g**(1/2))
for i in range(2, gf+1):
    if g%i==0:
        b.append(i)
        b.append(g//i)
b.append(g)
b=list(set(b))
b.sort()
for i in b:
    print(i, end=' ')

# 모범 답안
import sys
input = sys.stdin.readline


def gcd(a, b):
    return gcd(b, a % b) if a % b else b


n = int(input())
num = sorted([int(input()) for _ in range(n)])
get = num[1] - num[0]

for i in range(2, n):
    get = gcd(get, num[i]-num[i-1])

res = set()
for i in range(2, int(get**0.5)+1):
    if get % i == 0:
        res.add(i)
        res.add(get//i)
res.add(get)
res = sorted(list(res))
print(' '.join(map(str, res)))
