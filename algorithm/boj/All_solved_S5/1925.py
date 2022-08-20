# [TIL][Python] Boj - No.1925 (삼각형)
## 제출일 : 2022.08.20 (19:00)
'''
평면상에 세 개의 점이 주어지면, 그 세 점으로 이루어지는 삼각형은 유일하게 결정된다. 
또는, 삼각형이 이루어지지 않기도 한다. 세 점의 좌표가 주어졌을 때 
다음에 따라 이 삼각형의 종류를 판단하는 프로그램을 작성하시오.

세 점이 일직선 위에 있으면 - ‘삼각형이 아님’  출력할 때는 X
세 변의 길이가 같으면 - ‘정삼각형’ 출력할 때는 JungTriangle
두 변의 길이가 같으면
가장 큰 각이 90°보다 크면 - ‘둔각이등변삼각형’ 출력할 때는 Dunkak2Triangle
가장 큰 각이 90°이면 - ‘직각이등변삼각형’ 출력할 때는 Jikkak2Triangle
가장 큰 각이 90°보다 작으면 - ‘예각이등변삼각형’ 출력할 때는 Yeahkak2Triangle
세 변의 길이가 모두 다르면
가장 큰 각이 90°보다 크면 - ‘둔각삼각형’ 출혁할 때는 DunkakTriangle
가장 큰 각이 90°이면 - ‘직각삼각형’ 출력할 때는 JikkakTriangle
가장 큰 각이 90°보다 작으면 - ‘예각삼각형’ 출력할 때는 YeahkakTriangle
'''

## 내 풀이
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

len_ab = (abs(b1-a1)**2+abs(b2-a2)**2)
len_bc = (abs(b1-c1)**2+abs(b2-c2)**2)
len_ac = (abs(c1-a1)**2+abs(c2-a2)**2)

length = [len_ab, len_bc, len_ac]
length2 = [len_ab**0.5, len_bc**0.5, len_ac**0.5]

length.sort()
length2.sort()
d = (length[0] + length[1])

tri = []
if length2[2] >= length2[1] + length2[0]:
    tri.append('X')
else:
    if length2[0] == length2[1] and length2[1] == length2[2]:
        tri.append('Jung')
    elif length2[0] == length2[1] or length2[1] == length2[2] or length2[2] == length2[0]:
        if d < length[2]:
            tri.append('Dunkak')
        elif d == length[2]:
            tri.append('Jikkak')
        else:
            tri.append('Yeahkak')
        tri.append('2')
    else:
        if d < length[2]:
            tri.append('Dunkak')
        elif d == length[2]:
            tri.append('Jikkak')
        else:
            tri.append('Yeahkak')
    tri.append('Triangle')

print(''.join(tri))

## 피드백

