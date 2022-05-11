# 문제 : 좌표 압축
# 제출일 : 2022.. (:)
'''
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 
이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
'''

# 내 풀이
a = int(input())
b = list(map(int, input().split()))

c = sorted(b)
d = list(set(c))
d.sort()
output = [0*i for i in range(a)]

for i in range(a):
    output[i] += d.index(b[i])

result = ' '.join(map(str, output))
print(result)

# 모범 답안
n = input()
nums = list(map(int, input().split(" ")))

arr = sorted(set((nums)))
num_dict = {n: i for i, n in enumerate(arr)}

print(" ".join([str(num_dict[num]) for num in nums]))