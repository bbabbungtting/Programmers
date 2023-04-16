s1 = "1111111"

answer = []

delete_zero = 0
count = 0

x=s1

while(len!=1):
    count += 1
    delete_zero += x.count("0")

    len = x.count("1")

    x = format(len,'b')

answer.append(count)
answer.append(delete_zero)

print(answer)
