# 문제 : 달팽이는 올라가고 싶다
'''
땅 위에 달팽이가 있다. 
이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 
하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 
또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 
며칠이 걸리는지 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a, b, c = list(map(int, input().split()))

d = (c-a)//(a-b)

if a == c:
    print(1)
elif a-b == 1:
    print(d+1)
elif c-a < a-b:
    print(2)
elif (d-1)*(a-b) <= c-a and c-a <= d*(a-b):
    print(d+1)
elif d*(a-b) < c-a:
    print(d+2)
    
# 모범 답안
a, b, c = map(int, input().split())
print((c-b-1) // (a-b) +1)