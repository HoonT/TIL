# 문제 : 하키
# 제출일 : 2022.05.29 (:)
'''
선수들의 위치가 주어질 때, 링크 안 또는 경계에 있는 선수가 총 몇 명인지 구하는 프로그램을 작성하시오.
'''

# 내 풀이
width, height, x, y, player = list(map(int, input().split()))
cnt = 0
for i in range(player):
    x1, y1 = map(int, input().split())
    if 0 <= x1-x <= width and 0 <= y1-y <= height:
        cnt += 1
    elif ((x1-x)**2) + (y1-(height/2)-y)**2 <= (height/2)**2:
        cnt += 1
    elif (x1-width-x)**2 + (y1-(height/2)-y)**2 <= (height/2)**2:
        cnt += 1

print(cnt)

# 모범 답안
g=lambda:map(int,input().split())
w,h,x,y,p=g()
f,c,r=lambda o,p:(o*o+p*p)<=r*r,lambda a,b:(x<=a<=x+w and y<=b<=y+h)or f(x-a,y+r-b) or f(x+w-a,y+r-b),h//2
print(sum(c(*g())for _ in range(p)))