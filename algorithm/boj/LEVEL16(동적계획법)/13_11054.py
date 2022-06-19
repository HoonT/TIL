# [TIL][Python] Boj - No.11054 (가장 긴 바이토닉 부분 수열)
# 제출일 : 2022.06.19 (13:00)
'''
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면,
그 수열을 바이토닉 수열이라고 한다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 
가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
n = int(input())
seq = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(n):
    for k in range(i):
        if seq[i] < seq[k]:
            dp[i] = max(dp[i], dp[k]+1)
            
print(max(dp))

## 피드백