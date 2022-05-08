# 문제 : 배수와 약수
# 제출일 : 2022.05. (:)
'''
각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 
배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.
'''

# 내 풀이
while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    else:
        if a%b == 0:
            print("multiple")    
        elif b%a == 0:
            print("factor")
        else:
            print("neither")

# 모범 답안
