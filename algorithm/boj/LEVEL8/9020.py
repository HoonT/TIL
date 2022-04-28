# 문제 : 골드바흐의 추측
'''
2보다 큰 짝수 n이 주어졌을 때, 
n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 
두 소수의 차이가 가장 작은 것을 출력한다.
'''

# 내 풀이
m = 1
n = 10001
suso_list = set()
a = [True for i in range(n)]
for i in range(2, int(n**0.5)+1):
    if a[i] == True:
        for j in range(2*i, n, i):
            a[j] = False
for i in range(m,n):
    if i>1 and a[i] == True:
        suso_list.add(i)
        
T = int(input())
for k in range(T):
    k = int(input())
    dic = {}
    for i in suso_list: 
        if k-i in suso_list:        
            if i <= k-i:                
                dic[(k-i)-i] = [i, k-i]      
            else:
                dic[i-(k-i)] = [k-i, i] 
            
    key_list = list(dic.keys())    
    print(dic[min(key_list)][0],dic[min(key_list)][1])