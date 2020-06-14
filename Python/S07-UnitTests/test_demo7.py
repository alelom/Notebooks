import pytest

from demo7 import *

def queen_move_test1():
    assert queen_move(4,2,6,3) == False #invalid

def queen_move_test2():
    assert queen_move(4,1,4,3) == True #valid vertical

def queen_move_test3():
    assert queen_move(2,2,3,2) == True #valid horizontal

def queen_move_test4():
    assert queen_move(4,4,6,6) == True #valid diagonal

def test_queen_move5():
    with pytest.raises(ValueError):
        assert queen_move(0,1,1,1)
