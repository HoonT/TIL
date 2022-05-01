# 문제 : 분배합
# 제출일 : 2022.. (:)
'''
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
d = []
def div_sum(a):
    b = []
    for i in str(a):
        b.append(i)
    return b

for i in range(a):
    c = i
    for n in range(len(div_sum(i))):
        c +=  (int(div_sum(i)[n]))
    if c == a:
        print(i)
        d += [1]
        break
if d.count(1) == 0:
    print(0)

# 모범 답안
