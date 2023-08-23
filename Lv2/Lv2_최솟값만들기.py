A = [2,1]
B = [4,3]

answer = 0

size =len(A)

A.sort()
B.sort(reverse=True)

for i in range(size):
    answer += A[i] * B[i]

print(answer)