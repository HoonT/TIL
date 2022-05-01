# 문제 : 덩치
# 제출일 : 2022.05.01 (11:00)
'''
여러분은 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력해야 한다.
'''

# 내 풀이
a = int(input())
c = [1]*a
d = []
for i in range(a):
    weight, height = list(map(int, input().split()))
    d += [weight, height]

for j in range(a):
    for k in range(a):
        if d[2*j+1] < d[2*k +1]:
            if d[2*j] < d[2*k]:
                c[j] += 1
print(' '.join(str(_) for _ in c))

# 모범 답안
N= int(input())

S = [list(map(int, input().split())) for i in range(N)]

for x1, y1 in S:
    result = 1
    for x2, y2 in S:
        if x1 < x2 and y1 < y2:
            result += 1


    print(result, end =' ')