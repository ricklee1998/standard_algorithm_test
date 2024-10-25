## 10진수를 2진수로 변환하기 ##
#O((logn)^2)
def solution(decimal):
  result = ""
  stack = []
  while decimal > 0:
    remainder =- decimal % 2
    stack.append(str(remainder))
    decimal //= 2
  while stack:
    result += stack.pop()
  return result




#O(logn)
def solution2(decimal):
  result = ""
  stack = []
  while decimal > 0:
    remainder =- decimal % 2
    stack.append(str(remainder))
    decimal //= 2
  result = "".join(stack)
  return result[::-1]
print(solution2(10))
print(solution2(27))
print(solution2(12345))