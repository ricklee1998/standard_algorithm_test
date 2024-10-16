from typing import List

class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = None

  def __str__(s):
    return "head is: %s, / next is: %s"%(s.val, s.next)

def odd_even_list(head):
  if head is None:
    print("None Head")
    return
  odd = head
  even = head.next
  even_head = head.next

  #even node가 None이거나 even.next node가 None이면 break
  while even and even.next:
    odd.next, even.next = odd.next.next, even.next.next
    odd, even = odd.next, even.next

  odd.next = even_head
  return head

list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list5 = ListNode(5)
 
head = list1
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
 
head = odd_even_list(head)
 
while head:
  print(head.val, end="")
  if head.next:
    print("->", end="")
  head = head.next