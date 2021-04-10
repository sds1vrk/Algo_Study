# 주사위 게임
# 주사위 눈 상금 출력

import sys
# sys.stdin=open("input.txt","r")

n=int(input())
array=[]
for i in range(n):
    kk=map(int,input().split())
    array.append(list(kk))

# print(array)

def count_su(x):
    cnt=0
    set_x=set(x)
    set_x=list(set_x)
    set_x.sort(reverse=True)
    new_array=[]
    # print("x",x)
    # print("set",set_x)
    for i in set_x:
        # print("i",i)
        kk=x.count(i)
        tu=(kk,i)
        new_array.append(tu)
    new_array.sort(reverse=True)

    # print("new_array",new_array)

    if new_array[0][0]==3:
        return 10000+new_array[0][1]*1000
    elif new_array[0][0]==2:
        return 1000+new_array[0][1]*100
    else :
        return new_array[0][1]


max_val=-29700000
for i in array:
    val=count_su(i)
    if max_val<val:
        max_val=val

print(max_val)