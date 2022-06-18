# [TIL][Python] Boj - No.11053 (가장 긴 증가하는 부분 수열)
# 제출일 : 2022.06.18 (14:30)
'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 
길이는 4이다.
'''

## 내 풀이
x = int(input())
list = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if list[i] > list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

## 피드백
