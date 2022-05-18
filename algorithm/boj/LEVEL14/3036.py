# 문제 : 링
# 제출일 : 2022.05.17 (21:00)
'''
링의 반지름이 주어진다. 
이때, 첫 번째 링을 한 바퀴 돌리면, 
나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.
'''

# 내 풀이
import sys
n = int(sys.stdin.readline().strip())
getNum = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
checkNum = list(map(int,sys.stdin.readline().split()))
for i in checkNum:
    if i in getNum:
        print(1)
    else:
        print(0)

# 모범 답안
import math
n = int(input())
dia = list(map(int, input().split()))
    
for i in range(1, n):
    gcd = math.gcd(dia[0], dia[i])
    print(str(dia[0]//gcd) + '/' + str(dia[i]//gcd))