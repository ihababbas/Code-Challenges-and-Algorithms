# Write your test here
from ast import List

from pkg_resources import empty_provider
import pytest

from challenge02 import MyQueue


def test_one():
    stack1 = MyQueue()
    stack1.push("((()))")
  
    actual = stack1.output()
    excepted = True
    assert excepted == actual

def test_tow():
    stack1 = MyQueue()
    stack1.push("[(hello)()]")
    actual = stack1.output()
    excepted = True
    assert excepted == actual
    
def test_three():
    stack1 = MyQueue()
    stack1.push("[(])")
    actual = stack1.output()
    excepted = False
    assert excepted == actual