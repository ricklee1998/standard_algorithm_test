## 괄호 회전하기 ##

def solution(arr):
  result = 0
  n = len(arr)
  for i in range(n):
    stack = []
    for j in range(n):
      c = arr[(i+j) % n]
      if c == "(" or c == "[" or c =="{":
        stack.append(c)
      else:
        if not stack:
          break
      
        if c==")" and stack[-1] == "(":
          stack.pop()
        elif c=="]" and stack[-1] == "[":
          stack.pop()
        elif c=="}" and stack[-1] == "{":
          stack.pop()
        else:
          break
    else:
      if not stack:
        result += 1
  return result

input_1 = "[](){}"
input_2 = "}]()[{"
input_3 = "}}}"
print(solution(input_1))
print(solution(input_2))
print(solution(input_3))