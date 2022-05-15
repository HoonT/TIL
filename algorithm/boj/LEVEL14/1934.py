# 문제 : 최소공배수
# 제출일 : 2022.05.15 (10:18)
'''
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
import math
a = int(input())
for i in range(a):
    b, c = list(map(int, input().split()))
    print(math.lcm(b,c))

# 모범 답안
from sys import stdin

def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)
t = int(stdin.readline())
while t:
    a,b = map(int, stdin.readline().split())
    print(a*b//gcd(a,b))
    t-=1

