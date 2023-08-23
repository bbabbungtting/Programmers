def solution(s):
    tmp = []
    for x in s:
        #리스트 tmp에 문자 하나씩 삽입
        tmp.append(x)

        #리스트 tmp에 문자가 붙어 있을 경우 두랃 삭제
        if len(tmp) > 1 and tmp[-1] == tmp[-2]:
            tmp.pop()
            tmp.pop()

    if len(tmp)==0:
        return 1
    else:
        return 0