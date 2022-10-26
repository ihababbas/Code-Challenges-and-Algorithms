# Write your test here
from challenge03 import Node,LinkedList
import pytest

def test_zero():
  linkedList1 = LinkedList()
  node1 = Node("A")
  linkedList1.append(node1)
  node2 = Node("B")
  linkedList1.append(node2)
  node3 = Node("C")
  linkedList1.append(node3)
  node4 = Node("D")
  linkedList1.append(node4)
  linkedList1.deleteNode(2)
  actual= linkedList1.printAll()
  list =['A', 'B', 'D']
  excepted= print(list)
  assert excepted == actual

def test_one():
    linkedList2 = LinkedList()
    node5 = Node(1)
    linkedList2.append(node5)
    linkedList2.deleteNode(1)
    actual= linkedList2.printAll()
    list =[]
    excepted= print(list)
    assert excepted == actual
    
def test_tow():
    linkedList3 = LinkedList()
    node6 = Node(1)
    linkedList3.append(node6)
    node7 = Node(2)
    linkedList3.append(node7)
    linkedList3.deleteNode(1)
    actual=linkedList3.printAll()
    list =[1]
    excepted= print(list)
    assert excepted == actual