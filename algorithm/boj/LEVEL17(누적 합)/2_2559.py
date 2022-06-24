# [TIL][Python] Boj - No.2559 (수열)
## 제출일 : 2022.06.24 (14:30)
'''
매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 
연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.

매일 측정한 온도가 정수의 수열로 주어졌을 때, 
연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오. 
'''

## 내 풀이
N, K = map(int, input().split())
arr = list(map(int, input().split()))

tmp = sum(arr[:K])
result = tmp
for i in range(K, N):
    tmp += arr[i] - arr[i-K]
    result = max(result, tmp)

print(result)

## 피드백