# [TIL][Python] Boj - No.1059 (좋은 구간)
## 제출일 : 2022.07.25 (19:00)
'''
정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.

조건
1. A와 B는 양의 정수이고, A < B를 만족한다.
2. A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.

집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.
'''

## 내 풀이
l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.append(0)
s.sort()

A = 0
for i in range(len(s)-1) :
    if s[i] == n or s[i+1] == n:
        A = 0
        break
    elif s[i] < n and n < s[i+1]:
        A = (n - s[i]) * (s[i+1] - n) - 1
        break

print(A)

## 피드백