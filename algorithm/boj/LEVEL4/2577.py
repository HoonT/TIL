# 기찍 N
'''
세 개의 자연수 A, B, C가 주어질 때 
A * B * C를 계산한 결과에 0부터 9까지 
각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
b = int(input())
c = int(input())
i = 0
d = list(map(int, str(a*b*c)))

while i != 10:
    print(d.count(i))
    i += 1
    if i == 10:
        break

# 모범 답안
a = int(input())
b = int(input())
c = int(input())

d = list(map(int, (str(a * b * c))))

for i in range(10):
    print(d.count(i))
