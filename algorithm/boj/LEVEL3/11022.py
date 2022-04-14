# A+B - 8
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''
# 내 풀이
import sys

n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(i+1, a, b, a + b))

# 모범 답안
