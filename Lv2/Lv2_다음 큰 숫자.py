def solution(n):
    answer = 0
    one_in_n = format(n,'b').count('1')

    while(True):
        n+=1
        if(one_in_n== format(n,'b').count('1')):
            answer = n
            break
    return answer