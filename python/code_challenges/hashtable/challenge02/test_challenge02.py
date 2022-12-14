# Write your test here
import pytest

from challenge02 import firstRepeat


def test_zero():
  ex1 = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
  actual = firstRepeat(ex1)
  excepted= "ASAC"
  assert excepted == actual

def test_one():
  ex1 = "I am learning programming at ASAC."
  actual = firstRepeat(ex1)
  excepted= "No Repetition"
  assert excepted == actual