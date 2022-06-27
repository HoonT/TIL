# [TIL][Python] Boj - No.11660 (구간 합 구하기 5)
## 제출일 : 2022.06.27 (14:30)
'''
N×N개의 수가 N×N 크기의 표에 채워져 있다. 
(x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. 
(x, y)는 x행 y열을 의미한다.

표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 
이를 처리하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0 for i in range(N + 1)] for i in range(N + 1)]
seq = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + seq[i][j]
        
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))

## 피드백