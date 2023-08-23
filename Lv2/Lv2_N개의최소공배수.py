arr = [2,6,8,14]

sum =1

for i in range(len(arr)):
    sum *= arr[i]

answer = sum

for i in range(sum,arr[i-1],-1):
    flag = True
    for j in range(len(arr)):
        if(i%arr[j] != 0):
            flag = False
            break
    if(flag):
        answer = i

print(answer)