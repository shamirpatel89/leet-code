import math
from re import X
from turtle import right
from unittest import TestCase

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rights = n-1
        downs = m-1
        path_size = rights + downs

        return int(math.factorial(path_size) / (math.factorial(rights) * math.factorial(downs)))


class MyTest(TestCase):

    def test_(self):
        solution = Solution()
        cases = [
            [3, 7, 28],
            [3, 2, 3],
            [3, 3, 6],
            [23, 12, 3],
        ]

        for case in cases:
            with TestCase.subTest(self, m=case[0], n=case[1], expected=case[2]):
                self.assertEqual(case[2], solution.uniquePaths(case[0], case[1]))
