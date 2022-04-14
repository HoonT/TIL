# A+B - 5
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)
    
# 모범 답안
import sys
for k in sys.stdin:
    a,b=map(int,k.split())
    if a!=0 and b!=0:
        print(a+b)