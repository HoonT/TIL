# 문제 : 영화감독 숌
# 제출일 : 2022.05.03 (19:00)
'''
따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 
두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다. 
일반화해서 생각하면,
N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.
숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 
숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.
'''

# 내 풀이
new = []

def a(i):
    n = i*1000 + 666
    new.append(n)
    
def b(i):
    n = i//10 * 10000 + 666*10 + i%10
    new.append(n)

def c(i):
    n = i//100 * 100000 + 666 * 100 + i%100
    new.append(n)

def d(i):
    n = i//1000 * 1000000 + 666*1000 + i%1000
    new.append(n)

def s(i, n):
    n = 666 * n + i
    new.append(n)
    
result = []

arr = list(range(0, 10000))
for i in arr:
    a(i)
    if i//10 == 0:
        s(i, 10)
    if i//100 == 0:
        b(i)
        s(i,100)
    if i//1000 == 0:
        b(i)
        c(i)
        s(i, 1000)
    if i//10000 == 0:
        b(i)
        c(i)
        d(i)
        s(i, 10000)
        
result = list(set(new))
result.sort()

n = int(input(''))
print(result[n-1])

# 모범 답안
N = int(input())

def digit_666(num):
    s = 10;
    d = 0
    while int(num/s) >= 666:
        if int(num/s) % 1000 == 666:
            d = s
        s *= 10
    return d

title = 666
n = 1
while n < N:
    title += 1000
    d = digit_666(title)
    if d == 0:
        n += 1
    else:
        if (n + d >= N):
            title = int(title/d) * d
            title += (N - n - 1)
            n = N
        else:
            n += d
print(title)