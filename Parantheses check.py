# balanced
def parantheses_check(x):

    stack = []

    for i in x:
        if i in ['(', '{', '[']:
            stack.append(i)
        elif i in ['}', ']', ')']:
            if len(stack) == 0:
                return False
            elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
                stack.pop(-1)
            else:
                return False

    return len(stack) == 0

string1 = '{[()]}'
string2 = '{[)(]}'

print('string1', parantheses_check(string1))
print('string2', parantheses_check(string2))
