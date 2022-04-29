# 문제 : 네 번째 점
# 제출일 : 2022.04.28 (22:00)
'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 
네 번째 점을 찾는 프로그램을 작성하시오.
'''

# 내 풀이
a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
e, f = list(map(int, input().split()))
g = []
if a == c:
    g += [e]
elif a == e:
    g += [c]
elif e == c:
    g += [a]

if b == d:
    g += [f]
elif b == f:
    g += [d]
elif d == f:
    g += [b]

print(g[0],g[1])

# 모범 답안
x=y=0
exec("a,b=map(int,input().split());x^=a;y^=b;"*3)
print(x,y)