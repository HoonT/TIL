# 문제 : 파도반 수열
# 제출일 : 2022.06.10 (14:30)
'''
파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. 
P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.

N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.
'''

# 내 풀이
d = [0] * 101
d[0] = 1
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 2
for i in range(5, len(d)):
    d[i] = d[i-1] + d[i-5]

a = int(input())
for j in range(a):
    triangle = int(input())
    print(d[triangle-1])

# 모범 답안
from sys import stdin

P = [0, 1, 1, 1, 2, 2, 3]
for n in range(7, 101):
    P.append(P[n-1] + P[n-5])

next(stdin)
for n in map(int, stdin):
    print(P[n])