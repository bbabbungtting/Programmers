def solution(n):
    answer = 0
    
    x=0
    y=1
    for i in range(n-1):
        sum=x+y
        x = y
        y = sum
    answer = sum%1234567
    
    return answer