# 문제 : 팩토리얼
# 제출일 : 2022.04.29 (16:20)
'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
'''

# 내 풀이 1
import math
print(math.factorial(int(input())))

# 내 풀이 2
def factorial(a):
    if a == 1: return a
    if a == 0: return 1
    return a*factorial(a-1)
print(factorial(int(input())))