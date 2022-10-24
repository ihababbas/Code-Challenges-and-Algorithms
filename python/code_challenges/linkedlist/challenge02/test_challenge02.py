from ast import List
import pytest

from challenge02 import (
    Node,LinkedList
)

def test_zero():
  linkedList1 = LinkedList()
  linkedList1.push(5)
  linkedList1.push(4)
  linkedList1.push(3)
  linkedList1.push(2)
  linkedList1.push(1)
  actual= linkedList1.printMiddle()
  list = [3,4,5]
  excepted= print(list)
  assert excepted == actual
  
def test_zero():
  linkedList1 = LinkedList()
  linkedList1.push(6)
  linkedList1.push(5)
  linkedList1.push(4)
  linkedList1.push(3)
  linkedList1.push(2)
  linkedList1.push(1)
  actual= linkedList1.printMiddle()
  list = [4,5,6]
  excepted= print(list)
  assert excepted == actual