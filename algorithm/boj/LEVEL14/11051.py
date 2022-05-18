# 문제 : 이항 계수 2
# 제출일 : 2022.05.19 (08:15)
'''
자연수 N과 정수 K가 주어졌을 때 이항 계수 
nCk를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
import math

a, b = list(map(int, input().split()))

c = math.factorial(a)
d = math.factorial(b)
e = math.factorial(a-b)
f = c//(d*e)
print(f%10007)

# 모범 답안
n,k=map(int,input().split())
a=1
for i in range(k):a=a*(n-i)//(i+1)
print(int(a)%10007)