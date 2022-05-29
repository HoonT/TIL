# 문제 : 팩토리얼 0의 개수
# 제출일 : 2022.05.24 (10:40)
'''
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 
0의 개수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
import math

a = int(input())
b = math.factorial(a)
x = [int(k) for k in str(b)]
c = 0
for i in range(1,len(x)+1):
    if b%(10**i) == 0:
        c += 1
    else:
        break

print(c)

# 모범 답안
a=int(input())
print(a//5+a//25+a//125)