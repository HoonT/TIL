# [TIL][Python] Boj - No.1629 (곱셈)
## 제출일 : 2022.07.18 (17:00)
'''
자연수 A를 B번 곱한 수를 알고 싶다. 
단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input = sys.stdin.readline

a,b,c=map(int,input().split())

def times(a, b, c):
    if b == 1:
        return a%c
    
    x = times(a, b//2, c)
    if b%2 == 0:
        return (x * x) % c
    else:
        return (x * x * a) % c

d = times(a, b, c)
print(d)

## 피드백