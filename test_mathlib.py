from attr import __version_info__
import mathlib
import pytest
import sys

#@pytest.mark.skipif(sys.version_info < (3,5), reason="I don't want")
def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total == 9

def test_cal_multiply():
    result= mathlib.calc_multiply(10,3)
    assert result == 30

def test_dummy():
    assert True