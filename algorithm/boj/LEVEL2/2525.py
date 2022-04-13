#오븐 시계

a, b = map(int, input().split())
c = int(input())

x = a*60+b+c
print(x//60%24, x%60)