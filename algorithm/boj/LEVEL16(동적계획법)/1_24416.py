# 문제 : 알고리즘 수업 - 피보나치 수 1
# 제출일 : 2022.06.07 (13:00)
'''
재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 
아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.
'''

# 내 풀이
def fib(n):
    cnt = 0
    if n == 1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
print('{} {}'.format(fib(n), n-2))

# 모범 답안
N=int(input())
a=b=1
for _ in range(N-2):
    a,b=b,a+b
print(b,N-2)