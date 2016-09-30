from binarysearch import binary_search
from pytest import raises
# import numbers
# from fractions import Fraction
import numpy as np

# def test_mymath_mean():
#     assert myaverage([9,3]) == 6

        
# def test_char_median():
#     with raises(TypeError):
#         mymedian(['a', 3])

input = list(range(10))

def test_contains_NAN():
    with raises(NameError):
        binary_search([NAN,0], 0) 
        
def test_contains_char():
    with raises(TypeError):
        binary_search(['a',0], 0) 

def test_zero_elements():
    assert binary_search([], 0) == -1

def test_one_elements_found():
    assert binary_search([1], 1) == 0

def test_one_elements_not_found():
    assert binary_search([1], 0) == -1

def test_two_elements_found_at_left_edge():
    assert binary_search([0,1], 0) == 0

def test_two_elements_found_at_right_edge():
    assert binary_search([0,1], 1) == 1

def test_two_elements_not_found():
    assert binary_search([0,1], 2) == -1


def test_long_list_found_at_left_edge():
    assert binary_search(input, 0) == 0

def test_long_list_found_at_right_edge():
    assert binary_search(input, 9) == 9

def test_long_list_found_in_middle():
    assert binary_search(input, 5) == 5

def test_long_list_not_found_too_small():
    assert binary_search(input, -5) == -1

def test_long_list_not_found_too_large():
    assert binary_search(input, 11) == -1



def test_contains_inf_needle_inf():
    assert binary_search([1,2,np.inf], np.inf) == 2

def test_contains_inf_needle_normal_found():
    assert binary_search([1,2,np.inf], 2) == 1

def test_contains_inf_needle_normal_not_found():
    assert binary_search([1,2,np.inf], 3) == -1





#test left right parameter
# def test_left_custom_found():
#     assert binary_search(input, 2, 1) == 2

# def test_left_custom_not_found():
#     assert binary_search(input, 2, 4) == -1

def test_left_right_custom_found():
    assert binary_search(input, 2, 1, 6) == 2

def test_left_right_custom_not_found():
    assert binary_search(input, 8, 1, 6) == -1

def test_left_larger_than_right():
     assert binary_search(input, 2, 7, 6) == -1

def test_left_larger_equal_found():
     assert binary_search(input, 2, 2, 2) == 2

def test_left_larger_equal_not_found():
     assert binary_search(input, 5, 2, 2) == -1





