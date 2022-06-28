# [TIL][Python] Boj - No.11047 (동전 0)
## 제출일 : 2022.06.28 (15:30)
'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''

## 내 풀이
N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

cnt = 0
s = K

for coin in coins:
    cnt += s//coin
    s = s%coin

print(cnt)

## 피드백