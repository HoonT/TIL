# 문제 : 평균은 넘겠지
'''
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''

# 내 풀이
a = int(input())

for i in range(a):
    s = list(map(int, input().split()))
    
    b = s[0]
    c = sum(s[1:])
    e = round(c / b, 3)
    f = 0
    
    for n in range(1, b+1):
        if s[n] > e:
            f += 1
        g = round((f / b)*100, 3)
        h = '{:.3f}%'.format(g)
    print(h)
# 모범 답안
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    data = input().strip().split(' ')
    scores = list(map(float, data[1:]))
    average = sum(scores) / len(scores)

    above = 0
    for score in scores:
        if score > average:
            above += 1

    print(f'{(above/len(scores))*100:.3f}%')
