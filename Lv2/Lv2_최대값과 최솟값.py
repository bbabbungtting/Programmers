s1 = "1 2 3 4"
s2 = "-5 -3 -1 -2"

answer = ''

num_list = s1.split(' ')

num_list = list(map(int,num_list))

print(answer.join((str(min(num_list)),' ',str(max(num_list)))))