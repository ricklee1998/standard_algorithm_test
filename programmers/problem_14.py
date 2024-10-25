## 표 편집 ##
"""
UX 현재 선택한 행에서 X칸 위에 행 선택
DX 현재 선택한 행에서 X칸 아래 행 선택
C 현재 선택한 행 삭제후 바로 아래 행 선택, 단 삭제된 행이 가장 마지막 행인 경우 바로 윗행 선택
Z 가장 최근에 삭제한 행 원래대로 복구, 단 현재 선택한 행은 바뀌지 않음
"""

#O(n) //다시 풀어야함
def solution(n, k, cmd):
  all_state=["O"] * n
  live_node = n
  delete_stack=[]
  cur_col = k
  for cd in cmd:
    if cd[0] == "U":
      cur_col -= int(cd[2])
    elif cd[0] == "D":
      cur_col += int(cd[2])
    elif cd[0] == "C":
      delete_stack.append(cur_col)
      if cur_col == live_node - 1:
        cur_col -= 1
      live_node -= 1
    elif cd[0] == "Z":
      restore_col = delete_stack.pop()
      if cur_col > restore_col:
        cur_col += 1
      live_node += 1
  for d in delete_stack:
    all_state[d] = "X"
  return all_state



n=8
k=2
# cmd=["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
cmd=["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))