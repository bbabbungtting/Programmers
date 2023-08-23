s = "3people unFollowed me"
s1 = "for   the last week"

answer = ''

for i in range(len(s)):
    if(not(s[i].isdigit())): #문자일경우
        if(i==0): #첫번째
            answer += s[i].upper()
        else:
            if(s[i-1]==' '): #앞에 빈칸
                answer+=s[i].upper()
            else:
                answer+=s[i]
    else:
        answer += s[i]
    

print(answer)