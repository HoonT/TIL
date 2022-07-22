# [TIL][Python] Boj - No.11444 (피보나치 수 6)
## 제출일 : 2022.07.22 (22:00)
'''
피보나치 수는 0과 1로 시작한다. 
0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''

## 내 풀이
import sys
input=sys.stdin.readline
p=1000000007

def func(fibo,n):
    if n==1:
        return fibo
    elif n%2:
        return multi(func(fibo,n-1),fibo)
    else:
        return func(multi(fibo,fibo),n//2)

def multi(a,b):
    temp=[[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum=0
            for k in range(2):
                sum+=a[i][k]*b[k][j]
            temp[i][j]=sum%p
    return temp

fibo=[[1,1],[1,0]]
start=[[1],[1]]
n=int(input())
if n<3:
    print(1)
else:
    print(multi(func(fibo,n-2),start)[0][0])

## 피드백