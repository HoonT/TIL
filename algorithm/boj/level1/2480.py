# 주사위 세개

# 내 풀이
a, b, c = map(int, input().split())
if a == b and b == c:
    print(10000+(a*1000))
elif a != b and b != c and a != c:  #a!=c도 넣을 것
    if a > b and a > c:
        print(a*100)
    elif b > a and b > c:
        print(b*100)
    else:
        print(c*100)
else:
    if a == b:
        print(1000+(a*100))
    elif a == c:
        print(1000+(a*100))
    elif b == c:
        print(1000+(b*100))
        
# 모범답안
#1.
*_, a, b, c = sorted(input()); print(['1'+b,c][a<b<c]+'000'[a<c:])
#2.
a,b,c=sorted(map(int,input().split()))
print([c,b+10,b*10+100][[a,b,c].count(b)-1]*100)