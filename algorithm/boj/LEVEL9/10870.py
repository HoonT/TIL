# 문제 : 피보나치 수 5
# 제출일 : 2022.04.29 (:)
'''
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
b = [0, 1]

if a <= 1:
    print(a)
elif a > 1:
    for i in range(a-1):
        b += [b[len(b)-1] + b[len(b)-2]]   
    print(b[len(b)-1])

# 모범 답안
def r(x):
    if x < 2: return x
    return r(x-1)+r(x-2)
print(r(int(input())))