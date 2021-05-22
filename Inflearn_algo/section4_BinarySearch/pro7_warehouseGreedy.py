# 창고정리
# 그리디
import sys
# sys.stdin=open("input.txt","r")
n=int(input())

a=list(map(int,input().split()))
m=int(input())

# print(a)

res=0

a.sort(reverse=True)
# print("a",a)

for i in range(m):
    max_val=max(a)
    min_val=min(a)

    a.remove(max_val)
    a.remove(min_val)

    a.insert(0,max_val-1)
    a.insert(-1,min_val+1)

    if i==(m-1):
        print(max(a)-min(a))



