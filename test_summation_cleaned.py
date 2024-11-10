#Dummy pytest to work it out

import numpy as np

def summation(array):
    if array == []:
        return None
    else:
        return np.sum(array)
    
def test_summation():
    numbers = [1, 3, 5, 9]
    result = summation(numbers)
    assert result == 18
    
    #numbers = [1, 6, 5, 9]
    #result = summation(numbers)
    #assert result == 18
    
    empty_list = []
    result = summation(empty_list)
    assert result == None
