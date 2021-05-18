from typing import List
from unittest import TestCase

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x1, x2 = 0, len(matrix[0]) - 1
        y1, y2 = 0, len(matrix) - 1

        result = []

        while x1 <= x2 and y1 <= y2:
            width, height = x2 - x1 + 1, y2 - y1 + 1

            # top row
            i = x1
            while i <= x2:
                result.append(matrix[y1][i])
                i += 1

            # right column
            if height > 2:
                i = y1 + 1
                while i < y2:
                    result.append(matrix[i][x2])
                    i += 1

            # bottom row
            if height > 1:
                i = x2
                while i >= x1:
                    result.append(matrix[y2][i])
                    i -= 1

            # left column
            if width > 1 and height > 2:
                i = y2 - 1
                while i > y1:
                    result.append(matrix[i][x1])
                    i -= 1

            x1 += 1
            x2 -= 1
            y1 += 1
            y2 -= 1

        return result

    def spiralOrderOriignal(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        if len(matrix) == 1:
            return matrix[0]

        width = len(matrix[0])
        height = len(matrix)

        result = matrix[0]
        row = 1
        while row < height - 1:
            result.append(matrix[row][-1])
            row += 1

        result.extend(matrix[-1][::-1])

        row = height - 2
        if width > 1:
            while row > 0:
                result.append(matrix[row][0])
                row -= 1

        next = [
            row[1:-1]
            for row in matrix[1:-1]
        ]

        return result + self.spiralOrder(next)


class Test(TestCase):
    def test(self):
        cases = [
            [[[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]],
            [[[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]],
            [[[1,2,3]], [1,2,3]],
            [[[1]], [1]],
            [[[1,2],[3,4]], [1,2,4,3]],
            [[[1], [2], [3], [4]], [1, 2, 3, 4]],
            [[[1,2], [3,4], [5,6], [7,8]], [1,2,4,6,8,7,5,3]]
        ]

        solution = Solution()
        for case in cases:
            with self.subTest(case):
                expected = case[1]
                actual = solution.spiralOrder(case[0])

                self.assertEqual(expected, actual)
