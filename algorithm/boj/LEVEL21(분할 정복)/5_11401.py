# [TIL][Python] Boj - No.11401 (이항 계수 3)
## 제출일 : 2022.07.19 (21:30)
'''
자연수 N과 정수 K가 주어졌을 때 이항 계수 
nCk 를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
read = sys.stdin.readline

def cal(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (cal(a, b//2) ** 2 * a) % p
    else:
        return (cal(a, b//2) ** 2) % p

p = 1000000007
N, K = map(int, read().split())

num = [1 for _ in range(N+1)]

for i in range(2, N+1):
    num[i] = num[i-1] * i % p

A = num[N]
B = (num[N-K] * num[K]) % p

print((A % p) * (cal(B, p-2) % p) % p )

## 피드백