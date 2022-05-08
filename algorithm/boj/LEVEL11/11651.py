# 문제 : 좌표 정렬하기 2
# 제출일 : 2022.05.08 (09:00)
'''
2차원 평면 위의 점 N개가 주어진다. 
좌표를 y좌표가 증가하는 순으로, 
y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
import sys
input = sys.stdin.readline

a = int(input())
b = []
for i in range(a):
    x, y = list(map(int, input().split()))
    b += [[y, x]]
b.sort()

for k in range(a):
    print('{} {}'.format(b[k][1], b[k][0]))

# 모범 답안
from sys import stdin, stdout

def key(i):
    x,y=i.split()
    return int(x)/1000000+int(y)

i=stdin.readlines()[1:]

stdout.write(''.join(sorted(i, key=lambda x:key(x))))