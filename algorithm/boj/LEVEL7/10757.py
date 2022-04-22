# 문제 : 큰 수 A+B
'''
파이썬 같은 언어는 10,000자리 정도의 자연수도 자유롭게 다룰 수 있습니다. 
하지만 C/C++이라면 이 문제를 어떻게 풀까요?
'''

# 내 풀이
print(sum(list(map(int,input().split()))))

'''
이번 문제의 경우,
c/c++ java의 경우는 숫자 크기에 따라 변수 메모리를 더 많이
할당받아야 되는데,
파이썬, js는 자동으로 메모리를 관리해줘서 신경안써도 된다.
'''
