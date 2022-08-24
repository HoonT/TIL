# [TIL][Python] Boj - No.1300 (K번째 수)
## 제출일 : 2022.08.24 (16:00)
'''
세준이는 크기가 N×N인 배열 A를 만들었다. 
배열에 들어있는 수 A[i][j] = i×j 이다. 
이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. 
B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.
'''

## 내 풀이
n = int(input())
k = int(input())

start, end = 1, k

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in range(1,n+1):
        cnt += min(mid//i, n)
    if cnt >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)

## 피드백