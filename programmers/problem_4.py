## 모의고사 ##
# 1번 찍기: 1,2,3,4,5,1,2,3,4,5
# 2번 찍기: 2,1,2,3,2,4,2,5,   2,1,2,3,2,4,2,5
# 3번 찍기: 3,3,1,1,2,2,4,4,5,5,   3,3,1,1,2,2,4,4,5,5

"""시험은 최대 10000문제, 
문제의 정답 1,2,3,4,5 중 하나"""

#O(n)
def solution(answers):
  patterns = [
    [1,2,3,4,5], 
    [2,1,2,3,2,4,2,5], 
    [3,3,1,1,2,2,4,4,5,5]
  ]
  store_score = [0] * 3
  for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
      if answer == pattern[i % len(pattern)]:
        store_score[j] += 1

  max_score = max(store_score)
  highest_scores = []
  for i, score in enumerate(store_score):
    if score == max_score:
      highest_scores.append(i + 1)
  
  print(highest_scores)
  return highest_scores
input_1 = [1,3,2,4,2]



#O(n)
def solution2(answers):
  patterns = [
    [1,2,3,4,5], 
    [2,1,2,3,2,4,2,5], 
    [3,3,1,1,2,2,4,4,5,5]
  ]
  score = [0] * 3
  for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
      if answer == pattern[i % len(pattern)]:
        score[j] += 1

  max_score = max(score)
  highest_score = []
  for i, sc in enumerate(score):
    if max_score == sc:
      highest_score.append(i+1)

  print(highest_score)
  return highest_score

solution2(input_1)