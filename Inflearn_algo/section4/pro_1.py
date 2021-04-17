# 이분 검색
import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

a=list(map(int,input().split()))

# 정렬
a.sort()

# 이분 탐색
# 가운데 인덱스 찾고 값 찾기 ==> [i]가 찾을려는 값보다 크면 뒤에꺼 다 버리고, 앞에서 찾기, 다시 반복
# s는 start_idx, e는 end_idx, k는 mid 인덱스
# k=(s+e)//2 또는 k=((s+e)/2)

s,e=0,n-1
while True:

    # k=(s+e)//2
    k=int((s+e)/2)

    if a[k]==m:
        break

    elif a[k]<m:
        s=k+1

    else :
        e=k-1

# +1은 0번 인덱스부터 시자하므로 +1
print(k+1)