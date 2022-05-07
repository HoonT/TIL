# 문제 : 나이순 정렬
# 제출일 : 2022.. (:)
'''
이때, 회원들을 나이가 증가하는 순으로, 
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
b = []

for i in range(a):
    num, name = input().split()
    b += [[num, name]]

c = sorted(b)
for i in range(a-1):
    if c[i][0] == c[i+1][0]:
        if b.index(c[i]) > b.index(c[i+1]):
            temp = c[i]
            c[i] = c[i+1]
            c[i+1] = temp

for i in range(a):
    print('{} {}'.format(c[i][0], c[i][1]))

# 모범 답안
