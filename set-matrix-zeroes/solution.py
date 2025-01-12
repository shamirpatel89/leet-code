from unittest import TestCase
from typing import List, Tuple


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_columns = len(matrix[0])

        points: List[Tuple(int, int)] = []
        for row in range(num_rows):
            for column in range(num_columns):
                if matrix[row][column] == 0:
                    [points.append((row, y)) for y in range(0, num_columns)]
                    [points.append((x, column)) for x in range(0, num_rows)]

        for row, column in points:
            matrix[row][column] = 0

class MyTest(TestCase):

    def test_(self):
        solution = Solution()
        cases = [
            {
                'matrix': [[1,1,1],[1,0,1],[1,1,1]],
                'expected': [[1,0,1],[0,0,0],[1,0,1]],
            }
        ]

        for case in cases:
            with TestCase.subTest(self, **case):
                matrix = case['matrix']
                solution.setZeroes(matrix)
                self.assertEqual(matrix, case['expected'])
