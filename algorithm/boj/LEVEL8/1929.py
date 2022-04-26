# 문제 : 소수 구하기
'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
a, b  = list(map(int, input().split()))

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:          
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

c = prime_list(a)
d = prime_list(b+1)
e = sorted(list(set(d)-set(c)))
print(*e, sep='\n')

# 모범 답안
