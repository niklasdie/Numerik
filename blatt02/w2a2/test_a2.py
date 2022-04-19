"""
tests - well maybe just a single test - for a2 (the LU decomposition)


"""

import unittest
import numpy as np
from a2 import *
from logging import DEBUG, info, debug, basicConfig

basicConfig(level=DEBUG)


class TestLUDecomposition(unittest.TestCase):
    def test_lecture_examples(self):
        """
        This may be way too large for a unit test- but I don't care.
        """
        A = np.array(
            [
                [0, 0, 0, 1],
                [2, 1, 2, 0],
                [4, 4, 0, 0],
                [2, 3, 1, 0]
            ], dtype=np.float32
        )

        lu, p = zerlegung(A)

        debug(f"(lu,p):{(lu,p)}")

        b1 = np.array([3, 5, 4, 5])
        debug(f"b1:{b1}")
        c1 = permutation(p, b1)
        y1 = vorwaerts(lu, c1)
        x1 = rueckwaerts(lu, y1)

        equality = np.equal(
            x1,
            np.array([0, 1, 2, 3])
        ).all()
        debug(f"equality:{equality}")
        self.assertTrue(
            equality
        )

        b2 = np.array([4,10,12,11])
        c2 = permutation(p,b2)
        y2 = vorwaerts(lu,c2)
        x2 = rueckwaerts(lu,y2)

        self.assertTrue(
            np.equal(
                x2,
                np.array([1,2,3,4])
            ).all()
        )



