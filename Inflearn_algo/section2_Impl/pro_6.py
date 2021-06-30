#  자릿수의 합

import sys
# sys.stdin=open("3190.txt","rt")

n=int(input())

array=[i for i in map(int,input().split())]
# print(array)

result=[]
for i in array:
    kk=str(i)
    hap=0
    for j in range(len(kk)):
        hap+=int(kk[j])
    result.append(hap)

# print(result)
mm=max(result)
ii=result.index(mm)
print(array[ii])
