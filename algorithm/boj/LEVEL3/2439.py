# 별 찍기 - 2
'''
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
'''
# 내 풀이
n = int(input())
t = 1
list1 = ('*')

while t <= n:
    print(str(list1*t).rjust(n))
    t = t + 1
# 모범 답안
x= int(input())
for i in range(1,x+1):
    print(' '*(x-i)+'*'*i)