## 괄호 짝 맞추기 ##

def solution(s):
  stack = []
  for c in s:
    if c == ")" and stack[-1] == "(" and len(stack) > 0:
      stack.pop()
    else:
      stack.append(c)
  if len(stack) == 0:
    return True
  else:
    return False


input_1 = "(())()"
input_2 = "((())()"

print(solution(input_1))
print(solution(input_2))