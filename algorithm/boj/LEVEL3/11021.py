# A+B - 7
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
t = 1

while t <= a:
    b, c = map(int, input().split())
    print('Case #{}: {}'.format(t, b+c))
    t = t+1

# 모범 답안
import sys

n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d'%(i+1, a + b))