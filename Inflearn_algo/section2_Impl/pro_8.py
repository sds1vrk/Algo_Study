# 뒤집은 소수
# 뒤집은 수가 소수인지 확인


import sys
# sys.stdin=open("input.txt","r")

n=int(input())
array=list(map(int,input().split()))

def reverse(x):
    # print("test")
    return x[::-1]


def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

for i in array:
    kk=str(i)
    su=int(reverse(kk))
    # print("su",su)

    if su<=1:
        continue

    pan=isPrime(su)
    if pan:
        print(su, end=" ")




