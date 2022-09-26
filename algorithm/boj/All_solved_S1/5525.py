# [TIL][Python] Boj - No.5525 (IOIOI)
## 제출일 : 2022.09.26 (17:30)
### 알고리즘 : String
'''
N+1개의 I와 N개의 O로 이루어져 있으면, 
I와 O이 교대로 나오는 문자열을 PN이라고 한다.

P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)

I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, 
S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
'''

## 내 풀이
N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)

## 피드백