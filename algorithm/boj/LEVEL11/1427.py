# 문제 : 소트인사이드
# 제출일 : 2022.05.07 (10:00)
'''
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
'''

# 내 풀이
a = list(map(int, str(input())))
a.sort(reverse=True)
print(''.join(map(str, a)))

# 모범 답안
print(''.join(sorted(input())[::-1]))