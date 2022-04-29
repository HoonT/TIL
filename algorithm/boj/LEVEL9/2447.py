# 문제 : 별 찍기 - 10
# 제출일 : 2022.04.29 (:)
'''
크기 3의 패턴은 가운데에 공백이 있고, 
가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

N이 3보다 클 경우, 
크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)*(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
'''

# 내 풀이
a = int(input())

def star(a):
    if a == 3:
        return [['*','*','*'], ['*', ' ', '*'], ['*', '*', '*']]
    x = [[0]*a for i in range(a)]
    b = star(a//3)
    for i in range(a):
        for j in range(a):
            if i//(a//3) == j//(a//3) == 1:
                x[i][j] = ' '
            else:
                x[i][j] = b[i%(a//3)][j%(a//3)]
    return x
b = star(a)
for i in range(a):
    for j in range(a):
        print(b[i][j], end='')
    print(end='\n')

# 모범 답안
a=int(input())
def s(n):
 if n==3:return['***','* *','***']
 x=s(n//3)
 y=list(zip(x,x,x))
 for i in range(len(y)):y[i]=''.join(y[i])
 z=list(zip(x,[' '*(n//3)]*(n//3),x))
 for i in range(len(z)):z[i]=''.join(z[i])
 return y+z+y
print('\n'.join(s(a)))