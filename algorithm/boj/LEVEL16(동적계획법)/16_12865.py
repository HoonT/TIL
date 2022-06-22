# [TIL][Python] Boj - No.12865 (평범한 배낭)
## 제출일 : 2022.06.22 (15:00)
'''
준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 
각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 

준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
'''

## 내 풀이
#setting
N, K = list(map(int, input().split()))
put = [[0,0]]
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N):
    put.append(list(map(int, input().split())))

#method
for i in range(1,N+1):
    for j in range(1,K+1):
        if j < put[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-put[i][0]]+put[i][1])

#result     
print(dp[N][K])

## 피드백