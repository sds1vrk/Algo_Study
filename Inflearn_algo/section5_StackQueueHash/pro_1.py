# 스택 큐 해쉬

# 가장 큰 수 구하기
# 안되는 이유, find()로 하면 숫자가 겹치는 경우 가장 첫번째 인덱스인게 뽑아지기 때문에 안됨


import sys
sys.stdin=open("input.txt","r")

n,m=input().split()
m=int(m)

# n을 list로 변경
a=[]
for i in range(len(n)):
   a.append(int(n[i]))
print(a)
answer=[]
# print(m)

lt=0
rt=len(a)-m-1
# print("rt",rt)
answer_len=len(a)-m
# print("answer_len",answer_len)
while True:

    print("lt len(a)-rt+1",lt,len(a)-rt)

    # 첫번쨰 자리 찾기, 뒤에 4자리를 제외한것중에서 가장 큰 수 찾기
    max_value=-1
    for i in range(lt,len(a)-rt):
        print("a",a[i])
        if a[i]>=max_value:
            max_value=a[i]

    print(max_value)
    answer.append(max_value)
    # print(a.index(max_value))
    lt=a.index(max_value)+1
    # answer_len= len(a) - len(answer)
    rt=rt-1
    # print(rt)

    if len(answer)==answer_len:
        break


print(answer)







    # print(max_value)
















