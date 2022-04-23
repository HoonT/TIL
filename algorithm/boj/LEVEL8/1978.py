# 문제 : 소수 찾기
'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().split()))
c  = []
for i in range(a):
    if b[i] == 1:
        c += [1]
    else:
        for n in range(2,b[i]):
            if b[i]%n == 0:
                c += [2]
                break
            else:
                c += [3]
print(a-(c.count(1)+c.count(2)))

# 모범 답안
input();print(sum((10103**~-A%A<2)-(A in[1,561,645,946])for A in map(int,input().split())))