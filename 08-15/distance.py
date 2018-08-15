import math
import pytest

# p1 and p2 are tuples of size 2 (e.g., (1, 1))
def distance_2d(p1, p2):
    # returns a float!!!
    return math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )

def test_distance_2d_1():
    # assert(distance_2d((1,1), (2,2)) == math.sqrt(2)) # we can't do this
    assert(distance_2d((1,1), (2,2)) == pytest.approx(math.sqrt(2))) # we CAN do this

def test_distance_2d_2():
    assert(distance_2d((1,1), (1,1)) == pytest.approx(0.0))
