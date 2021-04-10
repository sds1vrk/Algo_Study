import sys
# sys.stdin=open("input.txt","rt")

# 리스트 만드는 방법 2가지
# array = [i for i in map(int, input().split())]
# array=list(map(int,input().split()))

t=int(input())

def kkk(n,s,e,k,text):
    new_text=text[s-1:e]
    new_text.sort()
    # print("new_",new_text.sort())
    # print("",new_text[k-1])
    return new_text[k-1]


for i in range(t):
    n,s,e,k=map(int,input().split())
    array=[i for i in map(int,input().split())]
    # 리스트 만드는 방법 2가지
    # array=list(map(int,input().split()))
    value=kkk(n,s,e,k,array)
    print("#%d %d"%(i+1,value))

# print(array)
