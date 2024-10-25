## 이진 탐색 트리 구현 ##

"""
lst 노드는 정수로 이루어져 있고 1000000 초과하지 않는다
이진 탐색 트리의 삽입과 탐색 기능을 구현
search_lst 길이는 10이하
"""

lst = [5,3,8,4,2,1,7,10]
search_lst = [1,2,5,6]


class Node:
  def __init__(self, key):
    self.left = self.right = None
    self.val = key

class BST:
  def __init__(self):
    self.root = None
  def insert(self, key):
    if not self.root:
      self.root = Node(key)
    else:
      curr = self.root
      while True:
        if key < curr.val:
          if curr.left:
            curr = curr.left
          else:
            curr.left = Node(key)
            break
        else:
          if curr.right:
            curr = curr.right
          else:
            curr.right = Node(key)
            break
  def search(self, key):
    curr = self.root
    while curr and curr.val != key:
      if key < curr.val:
        curr = curr.left
      else:
        curr = curr.right
    return curr
  
def solution(lst, search_lst):
  bst = BST()
  for key in lst:
    bst.insert(key)
  result = []
  for val in search_lst:
    if bst.search(val):
      result.append(True)
    else:
      result.append(False)

  return result


print(solution(lst, search_lst))