# Write your test here
from ast import List

from pkg_resources import empty_provider
import pytest

from challenge01 import MyQueue


def test_empty():
    stack = MyQueue()
    actual = stack.empty()
    excepted = True
    assert excepted == actual

def test_push():
    stack = MyQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.empty()
    excepted = False
    assert excepted == actual
    
def test_pop():
    stack = MyQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.pop()
    excepted = 1
    assert excepted == actual
    
def test_peek():
    stack = MyQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.peek()
    excepted = 1
    assert excepted == actual
    
def test_peek_pop():
    stack = MyQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    actual = stack.peek()
    excepted = 2
    assert excepted == actual