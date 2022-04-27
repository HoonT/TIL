# 문제 : 베르트랑
'''
자연수 n이 주어졌을 때, 
n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
'''

# 내 풀이
def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:          
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

for k in range(10000000):
    a = int(input())
    if a == 0:
        break
    else: 
        b = 2*a
        c = prime_list(a+1)
        d = prime_list(b+1)
        e = sorted(list(set(d)-set(c)))
        print(len(e))
        
# 모범 답안
