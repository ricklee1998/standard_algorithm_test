## 주식 가격##
#O(n)
"""
prices의 각 가격은 1~10000
prices의 길이 2~100000
"""

input_1 = [1,2,3,2,3]
input_2 = [1,6,9,5,3,2,7]
input_3 = [1,6,9,7,3,2,7]
# O(n)
def solution(prices):
  n = len(prices)
  answer = [0] * n
  stack = [0]
  for i in range(1, n):
    while stack and prices[i] < prices[stack[-1]]:
      j = stack.pop()
      answer[j] = i - j
    stack.append(i)
    # print("step1-1", i, answer)
    # print("step1-2", stack)
  # print(stack)
  while stack:
    j = stack.pop()
    answer[j] = n - 1 - j
  return answer

print(solution(input_1))
print(solution(input_2))
print(solution(input_3))

"""
input_3 = [1,6,9,7,3,2,7]
answer=[0,0,0,0,0,0,0]
stack=[0]

i=1 6<1
stack=[0,1]

i=2 9<6
stack=[0,1,2]

i=3 7<9
j=2 stack=[0,1]
answer=[0,0,1,0,0,0,0]
stack=[0,1,3]

i=4 3<7
j=3 stack=[0,1]
answer=[0,0,1,1,0,0,0]
i=4 3<6
j=1 stack=[0]
answer=[0,3,1,1,0,0,0]
stack=[0,4]

i=5 2<3
j=4 stack=[0,1]
answer=[0,0,1,1,1,0,0]
stack=[0,5]

i=6 7<2
stack=[0,5,6]

answer=[6,3,1,1,1,1,0]
"""