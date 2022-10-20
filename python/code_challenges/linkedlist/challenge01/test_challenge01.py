# Write your test here
from ast import List
import pytest

from challenge01 import (
    Node,LinkedList
)

def test_zero():
  linkedList1 = LinkedList()
  node1 = Node("A")
  linkedList1.append(node1) 
  node2 = Node("B")
  linkedList1.append(node2)
  node3 = Node("C")
  linkedList1.append(node3)
  linkedList1.delete("A")
  actual= linkedList1.printAll()
  list = ['B' , 'C']
  excepted= print(list)
  assert excepted == actual
  
  
def test_one():
  linkedList1 = LinkedList()
  node1 = Node("A")
  linkedList1.append(node1) 
  node2 = Node("B")
  linkedList1.append(node2)
  node3 = Node("C")
  linkedList1.append(node3)
  linkedList1.delete("B")
  actual= linkedList1.printAll()
  excepted= print("A\n" "C")
  assert excepted == actual
  
def test_tow():
  linkedList1 = LinkedList()
  node1 = Node("A")
  linkedList1.append(node1) 
  node2 = Node("B")
  linkedList1.append(node2)
  node3 = Node("C")
  linkedList1.append(node3)
  linkedList1.delete("C")
  actual= linkedList1.printAll()
  excepted= print("A\n" "B")
  assert excepted == actual

def test_three():
  linkedList1 = LinkedList()
  node1 = Node("A")
  linkedList1.append(node1) 
  node2 = Node("B")
  linkedList1.append(node2)
  node3 = Node("C")
  linkedList1.append(node3)
  linkedList1.delete("D")
  actual= linkedList1.printAll()
  excepted= print("A\n" "B\n" "C")
  assert excepted == actual

def test_four():
  linkedList1 = LinkedList()
  node1 = Node(4)
  linkedList1.append(node1) 
  node2 = Node(5)
  linkedList1.append(node2)
  node3 = Node(1)
  linkedList1.append(node3)
  node4 = Node(9)
  linkedList1.append(node4)
  linkedList1.delete(1)
  actual= linkedList1.printAll()
  list = [4,5,9]
  excepted= print(list)
  assert excepted == actual
  
  
def test_five():
  linkedList1 = LinkedList()
  node1 = Node(4)
  linkedList1.append(node1) 
  node2 = Node(5)
  linkedList1.append(node2)
  node3 = Node(1)
  linkedList1.append(node3)
  node4 = Node(9)
  linkedList1.append(node4)
  linkedList1.delete(5)
  actual= linkedList1.printAll()
  list = [4,1,9]
  excepted= print(list)
  assert excepted == actual
  
def test_six():
  linkedList1 = LinkedList()
  node1 = Node(4)
  linkedList1.append(node1) 
  node2 = Node(5)
  linkedList1.append(node2)
  node3 = Node(1)
  linkedList1.append(node3)
  node4 = Node(9)
  linkedList1.append(node4)
  linkedList1.delete(9)
  actual= linkedList1.printAll()
  list = [4,5,1]
  excepted= print(list)
  assert excepted == actual