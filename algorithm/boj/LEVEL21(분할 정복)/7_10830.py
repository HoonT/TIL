# [TIL][Python] Boj - No.10830 (행렬 제곱)
## 제출일 : 2022.07.21 (19:00)
'''
크기가 N*N인 행렬 A가 주어진다. 
이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.
'''

## 내 풀이
import sys
input = sys.stdin.readline

n, b = map(int, input().split())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))

def mulm(m1, m2):
    tmpArr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += m1[i][k] * m2[k][j] % 1000
            tmpArr[i].append(tmp)
    return tmpArr

def squarem(b):
    if b == 1:
        return m
    result = squarem(b//2)
    squareResult = mulm(result, result)
    if b % 2 == 0:
        return squareResult
    else:
        return mulm(squareResult, m)

for ans in squarem(b):
    for a in ans:
        print(a % 1000, end=" ")
    print()

## 피드백