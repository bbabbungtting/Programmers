answer = 1
    
for i in range(1,n):
    x = i
    sum = 0
    while(sum<n):
        sum += x
        x += 1
    if(sum==n):
        answer += 1