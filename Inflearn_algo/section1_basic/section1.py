# sep옵션은 띄어쓰기(공백)말고 다른 문자를 넣을수 있도록 함
# end는 다음 print문을 붙여서 사용할때 사용
print("test","hello","hi")
print("test","hello","hi",sep="")
print("test","hello","hi",sep="-")

print("testEnd",end="")
print("kkk")

# 문자열과 내장함수
# upper,lower는 return 값 존재, 원본은 있음
msg="It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

# 문자열에 해당 인덱스 번호 찾기 FIND
# 문자열에 찾을 문자열 몇개 인지 찾기 count
tmp=msg.upper()
print(tmp)
print(tmp.find("T"))
print(tmp.count("T"))
#0번 인덱스부터 (2-1)까지 문자열 추출
print(tmp[:2])
print(tmp[3:5])
print()

# 대문자, 소문자만 출력
for i in msg:
    if i.isupper():
        print(i,end="")
    # if i.islower():
    #     print(i,end="")
print()
# 알파벳만 출력
for x in msg:
    if x.isalpha():
        print(x,end="")
print()
# 아스키넘버 출력
# ord : 문자를 숫자로
# chr : 숫자를 문자로
tmp="AZ"
for x in tmp:
    print(ord(x))
print(chr(66))