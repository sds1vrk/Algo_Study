# 곶감 (모래시계)
# 행지정 해서 열 이동
# 오른쪽, 왼쪽 한칸 이동
# stack의 pop과 append를 활용

import sys
# sys.stdin=open("input.txt","r")

n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]
# print(a)

m=int(input())
b=[list(map(int,input().split())) for _ in range(m)]
# print(b)



def roate(h,v,m):

    # 왼쪽으로 이동
    if v==0:
        # 이동 횟수 만큼
        # 12 39 30 23 11 ==> 맨 처음꺼 빼서 맨 오른쪽으로 이동 * m번 만큼 반복
        for i in range(m):
            # a.append(a.pop(0))
            a[h-1].append(a[h-1].pop(0))

    # 오른쪽 이동
    elif v==1:
        # print("오른쪽 이동")
        # 맨 오른쪽 꺼 빼서 0번 인덱스 넣기
        # k=a[h-1].pop()
        # print("k",k)
        for i in range(m):
            a[h-1].insert(0,a[h-1].pop())

for i in b:
    h=i[0]
    v=i[1]
    m=i[2]

    roate(h,v,m)

# print(a)

# 회전을 하고 난 후 모래시계 모양에 숫자 뽑기
result=[]
s,e=0,n

for i in range(n):
    hap=0
    for j in range(s,e):
        hap+=a[i][j]

    result.append(hap)

    # 3행까지는 줄어든다. 다음 행에서는 s+1, e-1
    if i<n//2:
        # print("here")
        s+=1
        e-=1
        # print("s,e",s,e)
    else :
        # 4행 부터는 다시 s-1,e +1
        # print("asdf")
        s-=1
        e+=1
        # print(s,e)

# print(result)
print(sum(result))























