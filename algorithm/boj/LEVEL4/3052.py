# 기찍 N
'''
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
s = []
for i in range(10):
    a = int(input())
    if a%42 not in s:
        s += [a%42]
print(len(s))

# 모범 답안
b = [int(input())%42 for i in range(10)]
print(len(set(b)))