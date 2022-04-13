# N찍기
'''
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())

for i in range(1, a+1):
    print(i)

# 모범 답안
n = range(1,int(input())+1)
print('\n'.join(map(str,n)))