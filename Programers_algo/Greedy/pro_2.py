import re
def solution(name):
    # name 지정 idx, 이동 횟수 지정
    idx,count=0,0
    # 'A'를 제외한 모든 문자를 정규식으로 표현
    p=re.compile('[B-Z]')


    while True:
        # B-Z까지 외에 다른 문자열이 속해 있는지 확인
        m=p.search(name)
        if m:
            num=ord(name[idx])
            # 조이스틱을 위로 옮기는 경우 num-65
            # 조이스틱을 아래로 옮기는 경우 91-num
            count+=min(num-65,91-num)
            name=name[:idx]+'A'+name[idx+1:]
            print("name",name)





# solution("BBABA")
# solution("JEROEN")
solution("JAN")