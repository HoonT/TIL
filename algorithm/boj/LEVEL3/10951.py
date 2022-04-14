# A+B - 4
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
import sys

for k in sys.stdin:
    a, b = map(int, k.split())
    print(a+b)
    
# 모범 답안
import sys

for line in sys.stdin:
    print(sum(map(int,line.split())))


