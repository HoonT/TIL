# 문제 : 분수찾기
'''
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())

def logic1(a):
    i = 1
    if a == 1:
        return i
    while (a*2) > i*(i+1):
        i += 1
        if (a*2) <= i*(i+1):
            return i
        
b = a - ((logic1(a)-1)*logic1(a))//2
if logic1(a)%2 == 1:
    print('{}/{}'.format(logic1(a)-(b-1), 1+(b-1)))
else:
    print('{}/{}'.format(1+(b-1),logic1(a)-(b-1)))

# 모범 답안
n=int(input());a=0
while n>0:a+=1;n-=a
print("%d/%d"%(1-n,a+n)[::a%2*2-1])