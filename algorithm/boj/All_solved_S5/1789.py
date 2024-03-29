# [TIL][Python] Boj - No.1789 (수들의 합)
## 제출일 : 2022.08.13 (16:00)
'''
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
'''

## 내 풀이
s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)

## 피드백