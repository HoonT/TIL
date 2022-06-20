# [TIL][Python] Boj - No.2565 (전깃줄)
## 제출일 : 2022.06.20 (14:30)
'''
전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 
전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 

남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
n = int(input())
line = []
re_line = []
dp = [0 for i in range(n)]
for i in range(n):
    line.append(list(map(int, input().split())))
line.sort(key = lambda x:x[0])
for i in range(n):
    re_line.append(line[i][1])
for i in range(n):
    for j in range(i):
        if re_line[i] > re_line[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))

## 피드백