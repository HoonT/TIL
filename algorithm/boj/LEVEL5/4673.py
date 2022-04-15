# 문제 : 셀프 넘버
'''
셀프넘버: 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자
생성자가 없는 수 = 셀프넘버
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

'''

# 내 풀이
def self_number():
    list1 = []
    for b in range(1,10000):
        c = b + (b//1000) + ( (b//100)%10 ) + ( (b//10)%10 ) + (b%10)
        if 1 <= c <= 10000:
            list1 += [c]
    list2 = (range(1, 10000))
    list3 = list(set(list2)-set(list1))
    return sorted(list3)

for i in self_number():
    print(i)

# 모범 답안
