# 빠른 A+B
'''
Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 
문자열을 저장하고 싶을 경우 
.rstrip()을 추가로 해 주는 것이 좋다.
'''

# 내 풀이
import sys

input()
s = list(sum(map(int, n.split())) for n in sys.stdin)

for n in s:
    print(n)