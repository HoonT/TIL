# [TIL][Python] Boj - No.2407 (조합)
## 제출일 : 2022.08.27 (20:00)
'''
nCm을 출력한다.
'''

## 내 풀이
from math import factorial
n, m = map(int, input().split())
print(factorial(n)//(factorial(m)*factorial(n-m)))

## 피드백