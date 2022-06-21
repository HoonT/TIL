# [TIL][Python] Boj - No.9251 (LCS)
## 제출일 : 2022.06.21 (14:00)
'''
LCS(Longest Common Subsequence, 
최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
'''

## 내 풀이
import sys
input = sys.stdin.readline

a = sys.stdin.readline().strip().upper()
b = sys.stdin.readline().strip().upper()

lcs = [[0]*(len(a)+1) for _ in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            
print(lcs[-1][-1])

## 피드백