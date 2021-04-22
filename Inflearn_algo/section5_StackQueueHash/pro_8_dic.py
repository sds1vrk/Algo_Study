# 딕셔너리

import sys
sys.stdin=open("input.txt","r")

n=int(input())
p=dict()

# key, value를 사용해서 먼저 dict에 저장
for i in range(n):
    word=input()
    p[word]=1

# 키값으로 저장되어 이미 저장되어 있는것은
# 키 값으로 찾기 때문에 빠르게 찾을수 있음 따라서 value를 0으로 만들어줌
for i in range(n-1):
    word=input()
    p[word]=0

for key,val in p.items():
    if val==1:
        print(key)


        