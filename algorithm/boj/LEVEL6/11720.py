# 문제 : 숫자의 합
'''
N개의 숫자가 공백 없이 쓰여있다. 
이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
'''

# 내 풀이
a = int(input())
number = int(input())
b = sum(map(int, str(number)))
print(b)

# 모범 답안
input();print(sum(map(int,input())))