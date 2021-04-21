# section 3 - 탐색 & 시뮬레이션 (String, 1차원, 2차원 리스트 탐색)

# 회문 문자열 검사
import sys
sys.stdin=open("input.txt","r")

n=int(input())
array=[]

def check(m):
    m=m.upper()
    reverse_m=m[::-1]
    # print("reverse_m",reverse_m)
    if m==reverse_m:
        return "YES"

    else :
        return "NO"


# 역순으로 비교
def check2(m):
    m=m.upper()
    size=len(m)
    # for ~ else : 다 돌고 안걸리면 else
    for j in range(size//2):
        if m[j]!=m[-1-j]:
            return "NO"

    else :
        return "YES"



for i in range(n):
    m=input()
    # name=check(m)
    name=check2(m)
    array.append(name)


# print(array)

for i in range(n):
    print("#%d %s"%(i+1,array[i]))




