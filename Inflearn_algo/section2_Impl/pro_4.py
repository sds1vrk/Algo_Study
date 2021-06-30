# 대표값 구하기

# 평균 구하기, 반올림은 round()
import sys
sys.stdin=open("../section1/3190.txt", "rt")

n=int(input())

# 파이썬의 round는 even_round 방식이라 정확한 반올림은 원래수에서 0.5를 더한 후에 int로 치환해서 사용
# avr=round(sum(array)/len(array))
array=list(map(int,input().split()))
value=sum(array)/len(array)+0.5
avr=int(value)

# print(avr)

new_array=[]

# for i in range(n):
#     new_array.append(abs(array[i]-avr))


for i,j in enumerate(array):
    new_array.append((i+1,abs(avr-array[i]),array[i]))

# print(new_array)
# 이떄 차이가 가장 작은 것을 기준으로 오름차순 정렬
new_array.sort(key=lambda x:x[1])
# print(new_array)

# 같은것 끼리 묶기
result=[new_array[0]]
gi=new_array[0]
for i in range(1,len(new_array)):
    if gi[1]==new_array[i][1] and gi[2]<new_array[i][2]:
        result.pop()
        result.append(new_array[i])
        break

print(avr,result[0][0])

# 람다를 이용해서 가장 큰 수 빼기
# result.sort(key=lambda x:x[0],reverse=True)
# print(result)


