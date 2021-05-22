# 씨름선수 (그리디)
import sys
# sys.stdin=open("input.txt","r")
n=int(input())
a=[]

for i in range(n):
    a.append(list(map(int,input().split())))

# print(a)

a_sort=sorted(a,key=lambda x:x[1],reverse=True)

# print(a_sort)

res=[]

res.append(a_sort.pop(0))
# print(a_sort)
def pan(k):

    for i in range(len(res)):
        if res[i][0]>k[0] and res[i][1]>k[1]:
            return False
    else :
        return True

for i in range(len(a_sort)):
    # res에 저장되어 있는 인자값과 비교해서, 하나라도 크면 append
    # 둘다 작으면 continue
    if pan(a_sort[i]):
        res.append(a_sort[i])

print(len(res))








