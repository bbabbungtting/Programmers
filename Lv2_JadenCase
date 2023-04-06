def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if(not(s[i].isdigit())): #문자일경우
            if(i==0): #첫번째
                answer += s[i].upper()
            else:
                if(s[i-1]==' '): #앞에 빈칸
                    answer+=s[i].upper()
                else:
                    if('a'<= s[i] and s[i] <= 'z'):
                        answer+=s[i]
                    else:
                        answer+=s[i].lower()
                    
        else:
            answer += s[i]
        
    return answer
