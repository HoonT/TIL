# 문제 : 어린 왕자
# 제출일 : 2022.05.28 (17:30)
'''
은하수 지도, 출발점, 
도착점이 주어졌을 때 어린 왕자에게 필요한 최소의 
행성계 진입/이탈 횟수를 구하는 프로그램을 작성해 보자.
'''

# 내 풀이
import math
import sys
input = sys.stdin.readline

cnt_test = int(input())
cnt = 0
for _ in range(cnt_test):
    x1,y1,x2,y2 = list(map(int, input().split()))
    cnt_circle = int(input())
    for _ in range(cnt_circle):
        c1,c2,r = list(map(int, input().split()))
        if (x1-c1)**2+(y1-c2)**2 <= r**2:
            cnt += 1
            if (x2-c1)**2+(y2-c2)**2 <= r**2:
                cnt -= 1
        if (x2-c1)**2+(y2-c2)**2 <= r**2:
            cnt += 1
            if (x1-c1)**2+(y1-c2)**2 <= r**2:
                cnt -= 1
    print(cnt)
    cnt = 0

# 모범 답안
import sys
for i in range(int(sys.stdin.readline())):
    cnt=0
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for n in range(int(sys.stdin.readline())):
        cx, cy, r = map(int, sys.stdin.readline().split())
        if (r**2 > (x1-cx)**2+(y1-cy)**2) != (r**2 > (x2-cx)**2+(y2-cy)**2):
            cnt += 1
    print(cnt)
