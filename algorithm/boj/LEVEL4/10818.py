# 기찍 N
'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''

# 내 풀이
import sys
a = int(input())
s = list(map(int, input().split()))
print('{} {}'.format(min(s), max(s)))

# 모범 답안
from sys import stdin
_, *a = map(int, stdin.buffer.read().split())
print(min(a), max(a))