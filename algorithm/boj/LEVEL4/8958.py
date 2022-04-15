# OX퀴즈
'''
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. 
O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())

for i in range(a):
    b = list(map(str, input().split('X')))
    n = 1
    s = 0
    for  n in range(len(b)):
        c = b[n].count('O')
        d = ( ( (c*(1+c)) // 2 ) )
        s += d
        n += 1
    print(s)

# 모범 답안
import sys
N = int(sys.stdin.readline())
for i in range(N):
    quiz_result = sys.stdin.readline()
    accum = 1
    score = 0
    for q in quiz_result:
        if q is 'O':
            score += accum
            accum += 1
        else:
            accum = 1
    print(score)
