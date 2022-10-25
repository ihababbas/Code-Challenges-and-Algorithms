from challenge01 import Node,LinkedList,delete_node
import pytest
def test_delete(ll):
  actual=ll.__str__()
  expected='4-->1-->9-->None'
  assert expected==actual

def test_delete_one(check):
  actual=check.__str__()
  expected='4-->5-->9-->None'
  assert expected==actual


@pytest.fixture
def ll():
  ll = LinkedList()
  a=Node(4)
  b=Node(5)
  c=Node(1)
  d=Node(9)
  ll.append(a)
  ll.append(b)
  ll.append(c)
  ll.append(d)
  delete_node(b)
  return ll
@pytest.fixture
def check():
  ll_test = LinkedList()
  a=Node(4)
  b=Node(5)
  c=Node(1)
  d=Node(9)
  ll_test.append(a)
  ll_test.append(b)
  ll_test.append(c)
  ll_test.append(d)
  delete_node(c)
  return ll_test