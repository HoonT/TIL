# 문제 : 크로아티아 알파벳
'''
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
'''

# 내 풀이
a = list(str(input()))
b = len(a)
list1 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=']
list2 = ['dz=']
list3 = ['z=']
c = []
n = 0
i = 0

if b == 1:
    print(1)
else:
    while n != b-1:
        if a[n] + a[n+1] in list1:
            c += [1]
        elif a[n] + a[n+1] in list3:
            c += [3]    
        n += 1
        if n == b-1:
            break
    while i != b-2:
        if a[i] + a[i+1] + a[i+2] in list2:
            c += [2]
        i += 1
        if i == b-2:
            break
    print(b-(c.count(1))-((c.count(2)))-(c.count(3)))

# 모범 답안
c=input().count;print(c('')-1-sum(map(c,['-','=','nj','lj','dz='])))