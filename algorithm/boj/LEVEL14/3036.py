# 문제 : 링
# 제출일 : 2022.05.17 (21:00)
'''
링의 반지름이 주어진다. 
이때, 첫 번째 링을 한 바퀴 돌리면, 
나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.
'''

# 내 풀이
import math

a = int(input())
b = list(map(int, input().split()))

for i in range(1,a):
    number1 = b[0]//math.gcd(b[0],b[i])
    number2 = b[i]//math.gcd(b[0],b[i])
    print('{}/{}'.format(number1,number2))

# 모범 답안
