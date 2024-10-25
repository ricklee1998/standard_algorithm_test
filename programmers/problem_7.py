## 방문 길이 ##
"""
max 좌표 (-5,-5)~(5,5)
"""

#O(n^2)
def solution(dirs):
  visited = set()
  arr = []
  cur_x = 0
  cur_y = 0
  for i in dirs:
    if i == "U":
      if cur_y == 5:
        #무시
        pass
      else:
        cur_y += 1

    elif i == "D":
      if cur_y == -5:
        #무시
        pass
      else:
        cur_y -= 1

    elif i == "L":
      if cur_x == -5:
        #무시
        pass
      else:
        cur_x -= 1

    elif i == "R":
      if cur_x == 5:
        #무시
        pass
      else:
        cur_x += 1
    #if [cur_x, cur_y, i] not in  arr:
      #arr.append([cur_x, cur_y, i])
    if i == "L" or i == "R":
      visited.add((cur_x, cur_y, "X"))
    else:
      visited.add((cur_x, cur_y, "Y"))
  print(visited)
  # print(arr)
  return len(visited)


input_1 = "ULURRDLLU"
input_2 = "LULLLLLLU"
print(solution(input_1))
