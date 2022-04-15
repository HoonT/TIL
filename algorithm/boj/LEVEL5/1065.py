# 문제 : 한수
'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, 
N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
'''

# 내 풀이
def hansu(h):
    if 1 <= h < 100:
        return h
    
    if 100 <= h < 1000:
        list2 = []
        for i in range(100, h+1):
            if (((i//10)%10) - (i//100)) == ((i%10)-((i//10)%10)):
                list2 += [i]
        return len(list2)+99
    
    if h == 1000:
        return 144

h = int(input())    
print(hansu(h))

# 모범 답안
print(sum(i<100 or i//10%10*2==i%10+i//100 for i in range(1,int(input())+1)))
