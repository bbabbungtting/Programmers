s1 = "()()"
s = ")()("

answer = True

parenthesis_stack = []

for i in range(len(s)):
    if(i==0 and s[i]!='('):
        answer = False
        break

    if(s[i] == '('):
        parenthesis_stack.append('1')
    else:
        parenthesis_stack.pop()

if(len(parenthesis_stack)!=0):
    answer = False

print(answer)
