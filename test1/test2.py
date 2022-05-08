a = int(input())
b = list(map(int, input().split()))

b.sort()
if len(b) > 1:
    print(b[0]*b[len(b)-1])
elif len(b) == 1:
    print(b[0]**2)