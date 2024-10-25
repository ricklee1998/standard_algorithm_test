## 크레인 인형 뽑기 게임 ##

"""
board는 2차원 5x5 ~ 30x30
board 각 칸에는 0 이상 100 이하 정수 (0은 빈 칸)
moves 배열 크기는 1~1000
moves 원소 크기 1이상 ~ 배열 길이
"""
#O(MN)
def solution(board, moves):
  n = len(board)
  result = 0
  stack = []
  for move in moves:
    for j in range(n):
      if board[j][move-1] != 0:
        #stack 체크
        now_pos = board[j][move-1]
        if stack and stack[-1] == now_pos:
          stack.pop()
          result += 2
        else: 
          stack.append(board[j][move-1])
        board[j][move-1] = 0
        break
    
  return result

#O(N^2+M)
def solution2(board, moves):
  n = len(board)
  lanes = [[] for _ in range(n)]
  result = 0
  stack = []
  for i in range(n-1,-1,-1):
    for j in range(n):
      if board[i][j]:
        lanes[j].append(board[i][j])
  for move in moves:
    if lanes[move-1]:
      now_pos = lanes[move-1].pop()
      if stack and stack[-1] == now_pos:
        stack.pop()
        result += 2
      else: 
        stack.append(board[j][move-1])
  return result
board = [
  [0,0,0,0,0],
  [0,0,1,0,3],
  [0,2,5,0,1],
  [4,2,4,4,2],
  [3,5,1,3,1],
  ]

mvs=[1,5,3,5,1,2,1,4]

print(solution2(board, mvs))