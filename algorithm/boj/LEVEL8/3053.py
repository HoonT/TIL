# 문제 : 택시 기하학
# 제출일 : 2022.04.29 (11:02)
'''
반지름 R이 주어졌을 때, 
유클리드 기하학에서 원의 넓이와, 
택시 기하학에서 원의 넓이를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
import math
 
a = int(input())
print(round(math.pi*(a**2), 6))
print(round(((2*a)**2)/2, 6))

# 모범 답안
n=int(input())**2;print(n*3.14159265359,n*2.0)