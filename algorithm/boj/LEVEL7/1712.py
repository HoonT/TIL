# 문제 : 손익분기점
'''
A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a = list(map(int, input().split()))

def break_even(a):   
    if  a[2] <= a[1]: #주의 : ZeroDivision Error
        return -1
    else:
        return (a[0]//(a[2]-a[1])+1)
        
print(break_even(a))
# 모범 답안
a,b,c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)