# 문제 : 계단 오르기
# 제출일 : 2022.06.14 (14:00)
'''
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
'''

# 내 풀이 - 런타임 에러(IndexError)
import sys
input = sys.stdin.readline
arr = []
dp = []

s = int(input())
for i in range(s):
    arr.append(int(input()))
    
dp.append(arr[0])
dp.append(arr[0]+arr[1]) # <- 만약 계단이 한개면 문제가 생긴다.
dp.append(max(arr[1]+arr[2], arr[0]+arr[2]))

for i in range(3, s):
    dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]))

print(dp.pop())

# 모범 답안 - stari[0]에 0을 넣어서 위에 발생하는 문제 대비
N = int(input())

stair = [0]
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2] 

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])  

    print(dp[N])