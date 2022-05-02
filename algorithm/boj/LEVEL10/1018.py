# 문제 : 체스판 다시 칠하기
# 제출일 : 2022.05.02 (23:00)
'''
지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''

# 내 풀이
a, b=map(int,input().split())#a 세로, b 가로
c=[]
ans1=[]
ans2=[]
k1=[]
k2=[]
for i in range(0,a):
    c.append(input())
for i in range(0,8):
    if i%2==0:
       ans1.append("BWBWBWBW")
       ans2.append("WBWBWBWB")#정답이될 체스판
    else:
       ans1.append("WBWBWBWB")
       ans2.append("BWBWBWBW")
for q in range(0,a-7):
        k1.append([0]*(b-7))#k1은 정답1,k2는 정답2기준
        k2.append([0]*(b-7))#칠해야할 수 저장 배열
for q in range(0,a-7):
    for p in range(0,b-7):
      for i in range(q,q+8):
          for j in range(p,p+8):
              if c[i][j]!=ans1[i-q][j-p]:
                  k1[q][p]+=1
              if c[i][j]!=ans2[i-q][j-p]:
                  k2[q][p]+=1#정답과 다르면 k1또는 k2 +1 
k1m=min(map(min,k1))#k1의 최소값
k2m=min(map(min,k2))#k2의 최소값
if k1m<k2m:#둘중 작은 것
    print(k1m)
else:
    print(k2m)

# 모범 답안
import sys
from itertools import accumulate as acc
input = sys.stdin.readline
n, m = map(int, input().split())
y = [[0]*(m+1)]
for i in range(n):
    ac = [0]
    ac.extend(acc([((s=='W')+i+j) % 2 for j, s in enumerate(input().rstrip())]))
    y.append([k + j for k, j in zip(ac, y[-1])])

res = 32
for i in range(n-7):
    for j in range(m-7):
        u = y[i+8][j+8]-y[i+8][j]-y[i][j+8]+y[i][j]
        res = min(res, u, 64-u)
print(res)