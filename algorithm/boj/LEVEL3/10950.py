# A + B -3

# 내 풀이
a = int(input())
#b, c = map(int, input().split())
t = 1

while t <= a:
    b, c = map(int, input().split())
    print(b+c)
    t = t+1
    
# 모범 답안
# 1.
import sys
input()
s = list(sum(map(int, n.split())) for n in sys.stdin)
for n in s:
    print(n)