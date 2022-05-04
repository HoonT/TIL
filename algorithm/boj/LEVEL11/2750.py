# 문제 : 수 정렬하기
# 제출일 : 2022.05.04 (19:30)
'''
시간 복잡도가 O(n²)인 정렬 알고리즘으로 풀 수 있습니다. 
예를 들면 삽입 정렬, 거품 정렬 등이 있습니다.
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''

# 내 풀이
# O(N^2)
a = int(input())
b = []
for i in range(a):
    b += [int(input())] 
print(*sorted(b), sep='\n')

# 모범 답안
import sys;s=sys.stdin.read;input()
l=sorted(map(int,s().split()))
print(*l,sep='\n')