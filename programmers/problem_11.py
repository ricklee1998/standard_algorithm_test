## 짝지어 제거하기 ##

"""
문자열 길이 1000000 이하 & 소문자로 이루어져있다
"""
input_1 = "baabaa"
input_2 = "cdcd"

def solution(s):
  stack = []
  for c in s:
    if stack and stack[-1] == c:
      stack.pop()
    else:
      stack.append(c)
  return int(not stack)

print(solution(input_1))
print(solution(input_2))