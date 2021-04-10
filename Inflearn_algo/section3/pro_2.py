# 숫자만 추출
# 뽑은 숫자와 약수 구하기

import sys
sys.stdin=open("input.txt","r")

n=input()
size=len(n)
array=[]
for i in range(size):
    if n[i].isdigit():
        array.append(int(n[i]))


print(array)

print(''.join(array))