# 문제 : 소인수분해
'''
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
c = []
i = 2
if a == 1:
    print('')
else:
    while i != a:
        if a%i == 0:
            c += [i]
            a = a//i
        else:
            i += 1

    c += [a]
    print(*c, sep='\n')
    
# 모범 답안
n = int(input())
i = 2
r = int(n ** 0.5)

while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)