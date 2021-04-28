# 람다함수
# 익명의 함수, 표현식
def plus(x):
    return x+1
print(plus(2))

# 람다함수로 변경
# 변수명=람다
plus_two=lambda x:x+2
print(plus_two(1))

a=[1,2,3]
print(list(map(plus,a)))

# 리스트와 람다함수 혼합
print(list(map(lambda x:x+1,a)))

# 람다 정렬
# sorted(data, key=lambda x : x[0]) ==> 첫번째 키 값을 이용하여 오름차순 정렬
data=[[55, 259], [1, 226], [2, 217], [58, 201], [61, 198]]
d = sorted(data, key = lambda x : x[0],reverse=True)
print(d)