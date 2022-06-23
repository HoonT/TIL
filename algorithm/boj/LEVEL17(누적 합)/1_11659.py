# [TIL][Python] Boj - No.11659 (구간 합 구하기 4)
## 제출일 : 2022.06.23 (15:30)
'''
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for n in range(1, N + 1):
    arr[n] = arr[n - 1] + arr[n]
for m in range(M):
    i, j = map(int, input().split())
    print(arr[j] - arr[i - 1])

## 피드백