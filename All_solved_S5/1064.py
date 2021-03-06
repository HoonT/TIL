# [TIL][Python] Boj - No.1064 (평행사변형)
## 제출일 : 2022.07.26 (22:30)
'''
평행사변형은 평행한 두 변을 가진 사각형이다. 
세 개의 서로 다른 점이 주어진다. A(xA,yA), B(xB,yB), C(xC,yC)

이때, 적절히 점 D를 찾아서 네 점으로 평행사변형을 만들면 된다. 
이때, D가 여러 개 나올 수도 있다.

만들어진 모든 사각형 중 가장 큰 둘레 길이와 
가장 작은 둘레 길이의 차이를 출력하는 프로그램을 작성하시오. 

만약 만들 수 있는 평행사변형이 없다면 -1을 출력한다.
'''

## 내 풀이
x1,y1,x2,y2,x3,y3 = map(int, input().split())

if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
    print(-1.0)
else: 
    case1 = ((x1-x2)**2+(y1-y2)**2)**(1/2) + ((x2-x3)**2+(y2-y3)**2)**(1/2)
    case2 = ((x1-x2)**2+(y1-y2)**2)**(1/2) + ((x1-x3)**2+(y1-y3)**2)**(1/2)
    case3 = ((x1-x3)**2+(y1-y3)**2)**(1/2) + ((x2-x3)**2+(y2-y3)**2)**(1/2)
    print(2*(max(case1, case2, case3)-min(case1, case2, case3)))

## 피드백