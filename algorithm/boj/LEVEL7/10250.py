# 문제 : ACM호텔
'''
여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에 
이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다. 
'''

# 내 풀이
count = int(input())

for i in range(count):
    a, b, c = list(map(int,input().split()))
    d = c//a
    e = c%a
    if c%a == 0:
        if d < 10:
            print('{}0{}'.format(a,d))
        else:
            print('{}{}'.format(a,d))        
    else:
        if d < 9:
            print('{}0{}'.format(e,d+1))
        else:
            print('{}{}'.format(e,d+1))
# 모범 답안
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    h,w,n = map(int,input().split())
    print(str((n-1)%h+1) + str((n-1)//h+1).rjust(2,'0')) 