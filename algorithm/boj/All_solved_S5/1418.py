# [TIL][Python] Boj - No.1418 (K-세준수)
## 제출일 : 2022.08.06 (13:00)
'''
오세준은 어떤 자연수의 소인수중 최댓값이 K보다 크지 않을때 그 수를 K-세준수라고 부른다.

N보다 작거나 같은 자연수 중에 K-세준수가 총 몇 개인지 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

s = [0 for i in range(n+1)]
for i in range(2,n+1):
    if s[i] == 0:
        for t in range(i,n+1,i):
            if t%i == 0:
                s[t] = max(s[t],i)
ans = 0
for i in s:
    if i <= m:
        ans += 1
print(ans-1)

## 피드백