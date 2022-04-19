"""
LU decomposition without special pivoting (just change if needed and use the 
first row with a non zero element in the right place)

I'll allways assume correct input
"""





from typing import Tuple

import numpy as np
import logging
from logging import debug

logging.basicConfig(level=logging.DEBUG)


def zerlegung(A : np.ndarray) ->Tuple[np.ndarray,np.ndarray]:
    """Decomposes the Matrix A 

    Returns the matrixes L and U in one matrix LU and the permutation vector.
    """
    # debug(f"A:{A}")

    A = A.copy() # yes, this is not necessary because we can use the slicing
    # in recursion, but it would be harder to debug

    # 0. base case for recursion
    if A.shape == (1,1):
        return A,[]

    

    # 1. switch rows if necessary
    if A[0,0] == 0:
        # finds row to switch with
        for row_index,value in enumerate(A):
            if value[0] != 0:
                switched_rows = row_index+1 # python start counting with 0!
                break
        # switch row 
        A = permutation_matrix_rows([switched_rows],A)
        
    else:
        switched_rows = 1

    # 2. eliminate column

    first_row = A[0]
    rows_after_the_first = A[1:]
    for row in rows_after_the_first:
        # compute the "elimination element" l_xy
        row[0] = row[0]/first_row[0]
        # adjust the rest of the row
        row[1:] = row[1:]-first_row[1:]*row[0]



    # 3. call yourself for the rest
    
    lu , p = zerlegung(A[1:,1:])

    # integrate the stuff from the recursion into A and p
    p = [value+1 for value in p] # increase each value by one 
    A = permutation_matrix_rows([1]+p,A) # permutate a by p
    p = [switched_rows]+p # append at the front
    A[1:,1:] = lu

    return A,p

def permutation(p,b):
    """returns P*b, i.e. the permutated vector b"""
    b = b.copy()

    for index, value in enumerate(p):
        value = value -1 # python start counting with 0!
        temp = b[index]
        b[index] = b[value]
        b[value] = temp

    return b

def permutation_matrix_rows(p,A):
    """Returns P*A"""
    b = A.copy() # yeah I was to lacy for refactoring

    for index, value in enumerate(p):
        value = value -1 # python start counting with 0!
        temp = b[index].copy()
        b[index] = b[value]
        b[value] = temp

    return b


def vorwaerts(LU : np.ndarray,c : np.ndarray):
    """solves Ly=c
    
    so c seems to be already permuted. Good!


    """
    c = c.copy()

    rows, columns = LU.shape

    for column in range(columns):
        for row in range(rows):
            # don't touch anything if we are not in the 
            # bottom triangle = continue if the column number is 
            # larger or equal to the row number
            if column >= row:
                continue

            # debug(f"touching LU[{row},{column}]={LU[row,column]}")
            c[row] = c[row] - LU[row,column]*c[column]


    return c



    

def rueckwaerts(LU,y):
    """solves Ux=y"""
    y  = y.copy()
    rows, columns = LU.shape

    for column in reversed(range(columns)):
        y[column] /= LU[column,column]
        for row in reversed(range(rows)):
            # don't touch anything if we are not in the 
            # top right triangle -> skip element if the 
            # column number is not larger than the row
            if column <= row:
                continue

            # debug(f"touching LU[{row},{column}]={LU[row,column]}")
            y[row] -= LU[row,column]*y[column] 

    return y


if __name__ == "__main__":

    print("For the test on the lecture example see test_a2.py")
    # TODO: test on generative system

    for n in [10,20,100]:
        pass

    