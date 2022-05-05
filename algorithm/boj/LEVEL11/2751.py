# 문제 : 수 정렬하기 2
# 제출일 : 2022.05.05 (10:00)
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''

# 내 풀이
import sys
input = sys.stdin.readline
a = int(input())
b = []
for i in range(a):
    b += [int(input())]
b.sort()    
print(*b, sep='\n')

