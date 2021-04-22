# 아나그램
# 딕셔너리 해쉬
# str1, str2 입력

# str1[A]=1
# str1[A]=str1[A]+1
# 이렇게 해버리면 키값이 없는 경우가 발생 가능
# 따라서 str1[A]=str1.get('A',0)+1 을 이용하여 없으면 str1[A] return, 없으면 0을 리턴


import sys
sys.stdin=open("input.txt","r")

n=list(input())
n.sort()
m=list(input())
m.sort()
n_dict=dict()

for x in n:
    # get을 이용해서 만약 키 값이 있으면 그걸 사용하고 없으면 0을 리턴
    n_dict[x]=n_dict.get(x,0)+1

for x in m:
    n_dict[x]=n_dict.get(x,0)-1

print(n_dict)
for x in n:
    # -1이 생김으로써 +1이 생길수 밖에 없기 떄문에 이게 가능
    # 내 생각엔 더 좋은건
    # if n_dict.get(x)!=0 인듯
    if n_dict.get(x)>0:
        print("NO")
        break
else :
    print("YES")