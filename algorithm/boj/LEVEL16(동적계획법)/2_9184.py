# 문제 : 신나는 함수 실행
# 제출일 : 2022.06.08 (13:00)
'''
a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
d = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <=0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    
    if d[a][b][c]:
        return d[a][b][c]
    elif a < b and b < c:
        d[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return d[a][b][c]

    else:
        d[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return d[a][b][c]

while 1:
    a,b,c = list(map(int, input().split()))
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a,b,c,w(a,b,c)))

# 모범 답안
