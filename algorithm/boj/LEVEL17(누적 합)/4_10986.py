# [TIL][Python] Boj - No.10986 (나머지 합)
## 제출일 : 2022.06.26 (14:30)
'''
수 N개 A1, A2, ..., AN이 주어진다. 
이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.
'''

## 내 풀이
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
seq = list(map(int, input().split()))

table = [0 for i in range(M)]
table_sum = 0
table[0] = 1
ans=0

for i in range(N):
    table_sum+=seq[i]
    table[table_sum%M] += 1
for i in table:
    ans += i*(i-1)//2

print(ans)

## 피드백