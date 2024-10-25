

"""
arr1, arr2 length 2~100
arr1, arr2 value -10 ~ 20
"""

#O(n^3)
def solution(arr1, arr2):
  r1, c1 = len(arr1), len(arr1[0]) #3,3 / 3,2
  r2, c2 = len(arr2), len(arr2[0]) #3,1 / 2,2
  answer = [[0] * c2 for _ in range(r1)]

  for i in range(r1):
    for j in range(c2):
      for k in range(c1):
        answer[i][j] += arr1[i][k] * arr2[k][j]

  return answer



arr_0_1 = [[1,2,3],[3,2,1],[2,2,2]]
arr_0_2 = [[5],[7],[4]]

arr_1_1 = [[1,4],[3,2],[4,1]]
arr_1_2 = [[3,3],[3,3]]

arr_2_1 = [[2,3,2],[4,2,4],[3,1,4]]
arr_2_2 = [[5,4,3],[2,4,1],[3,1,1]]

print(solution(arr_0_1, arr_0_2))
print(solution(arr_1_1, arr_1_2))