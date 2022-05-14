# 문제 : 검문
# 제출일 : 2022.. (:)
'''
먼저 근처에 보이는 숫자 N개를 종이에 적는다. 
그 다음, 종이에 적은 수를 M으로 나누었을 때, 
나머지가 모두 같게 되는 M을 모두 찾으려고 한다. 
M은 1보다 커야 한다.

N개의 수가 주어졌을 때, 가능한 M을 모
두 찾는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
b = []
d = []
c = []
for i in range(a):
    b += [int(input())]
    
b.sort()
for j in range(2,b[0]):
    for i in range(len(b)):
        c += [b[i] % j]
    if c.count(c[0]) == len(c):
        d += [j]
    c.clear()

print(*d, sep=' ')

# 모범 답안
