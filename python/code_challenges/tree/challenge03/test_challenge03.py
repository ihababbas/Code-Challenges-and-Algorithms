# Write your test here
import pytest

from challenge03 import TreeNode

def test_zero():
  test = TreeNode()
  actual= test.sortedArrayToBST([-10,-3,0,5,9])
  excepted= 0
  assert excepted == actual

def test_one():
  test = TreeNode()
  actual= test.sortedArrayToBST([3,1])
  excepted= 3
  assert excepted == actual