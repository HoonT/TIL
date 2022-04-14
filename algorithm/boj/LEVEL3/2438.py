# 별 찍기 - 1
'''
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
'''

# 내 풀이
n = int(input())
t = 1
list1 = ('*')

while t <= n:
    print(list1*t)
    t = t + 1
# 모범 답안
for i in range(1,int(input())+1): print('*'*i)