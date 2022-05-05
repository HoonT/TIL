# 문제 : 통계학
# 제출일 : 2022.. (:)
'''
N개의 수가 주어졌을 때, 네 가지 기본 통계값
(산술평균, 중앙값, 최빈값, 범위)
을 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())

b = []
for i in range(a):
    b += [int(input())]
   
def san(a):
    return round(sum(a)/len(a))
def joong(a):
    a.sort()
    return a[len(a)//2]
def choi(a):
    a.sort()
    b = [0 for i in range(len(a))]
    for i in range(len(a)):
        b[i] = a.count(a[i])
    for j in range(len(a)):
        if b[j] != max(b):
            a.pop(a[j])
    if len(a) > max(b):
        return a[max(b)]
    else:
        return a[0]
def bum(a):
    if len(a) == 1:
        return 0
    else:
        return max(a) - min(a)

c = b
e = b
d = b
print(san(b))
print(joong(c))
print(choi(d))
print(bum(e))


# 모범 답안
