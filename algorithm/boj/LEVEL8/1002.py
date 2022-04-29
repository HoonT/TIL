# 문제 : 터렛
# 제출일 : 2022.04.29 (13:05)
'''
조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

두 원의 위치관계 - 만나지 않은 경우, 외부에 있을 때, 동심원
'''

# 내 풀이
a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    from math import dist
    c1 = (b[0], b[1])
    c2 = (b[3], b[4])
    e = dist(c1,c2)
    r1 = abs(b[2]+b[5])
    r2 = abs(b[2]-b[5])
    if c1 == c2 and b[2] == b[5]:
        print(-1)
    else:
        if r1 < e or r2 > e or e == 0:
            print(0)
        elif r1 == e or r2 == e:
            print(1)
        elif r2 < e or e < r1:
            print(2)

# 모범 답안
T=int(input())
import sys
num=sys.stdin.readlines()
for i in num:
    x1,y1,r1,x2,y2,r2=map(int,i.split())
    dist=(((x1-x2)**2)+((y1-y2)**2))**0.5
    if dist>r1+r2: print(0)
    elif dist==r1+r2: print(1)
    elif abs(r1-r2)<dist<r1+r2:print(2)
    elif abs(r2-r1)==dist and r2==r1: print(-1)
    elif abs(r2-r1)==dist: print(1)
    else: print(0)
