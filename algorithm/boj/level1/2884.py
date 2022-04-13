# 알람 시계

#내 풀이
a, b = map(int, input().split())

if b < 45:
    if a > 1:
        print(a-1, 60-(45-b))
    elif a == 0:
        print(23+a, 60-(45-b))
    elif a == 1:
        print(0, 60-(45-b))
elif b >= 45:
    print(a, b-45)
    
# 모범 답안
a,b=map(int,input().split());x=a*60+b-45;print(x//60%24,x%60)