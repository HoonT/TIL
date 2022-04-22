# 문제 : 설탕 배달
'''
봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 
봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
b = a//5
list1 = []

for i in range(b+1):
    d = a-(5*i)
    if d%3 == 0:
        list1 += [(i+d//3)]

if list1 == []:
    print(-1)
else:
    print(min(list1))
    
# 모범 답안 1
n=int(input());print(-1if n in [1,2,4,7] else n//5+n%5-n%5//3*2)
# 모범 답안 2
i,c=int(input()),0
while i%5:i-=3;c+=1
print((i//5+c,-1)[i<0])
    