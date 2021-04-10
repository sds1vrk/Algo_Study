# 리스트와 내장함수 (1)
import random as r
# 리스트 range로 만들기
b=list(range(1,11))
print(b)
c=list(range(11,20))
# 리스트는 +로 합치기 가능
aa=b+c
print(aa)

# insert는 인덱스에 값 넣기
b.insert(9,"*")
print(b)

# pop은 뒤에꺼 빼기, 안에 숫자가 들어가면 인덱스를 뺼수 있음
b.pop()
print("b_pop",b)

b.pop(9)
print("b_pop_10",b)

# remove는 value 없애기
b.remove(9)
print(b)

# a.index(value)는 value의 해당 index 알려주기
print(b.index(8))

# sum 리스트에 값을 다 더하기
a=list(range(1,11))
print(a)
print(sum(a))
print("min",min(a))
# min으로 둘중에 작은 수 찾기, 리스트 중에 작은 리스트 찾기
print(min(a[:3],a[3:]))

# shuffle
r.shuffle(a)
# sort
# 오름차순
a.sort()
print(a)
# 내림차순
a.sort(reverse=True)
print(a)