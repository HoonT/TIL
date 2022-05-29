# 문제 : 나는야 포켓몬 마스터 이다솜
# 제출일 : 2022.05.21 (17:00)
'''
1. 입력 : 도감 수, 문제의 개수
2. 출력 : 문제의 답(숫자 -> 이름, 이름 -> 숫자)
'''

# 내 풀이
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dic = {}
for i in range(1, N+1):
    name = input().rstrip()
    dic[name] = str(i)
    dic[str(i)] = name

for _ in range(M):
    print(dic[input().rstrip()])

# 모범 답안
import sys
def sol():
	input=sys.stdin.readline
	n,m=map(int,input().split())
	d={}
	dd=[];dda=dd.append
	for i in range(1,n+1):
		t=input().strip()
		d[t]=str(i)
		dda(t)
	ans=[]
	aa=ans.append
	for i in range(m):
		t=input().strip()
		if t.isdigit():
			aa(dd[int(t)-1])
		else:
			aa(d[t])
	print("\n".join(ans))
sol()