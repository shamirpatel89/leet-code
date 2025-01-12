from unittest import TestCase

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        negative = 1

        if dividend < 0:
            dividend *= -1
            negative *= -1

        if divisor < 0:
            divisor *= -1
            negative *= -1

        if divisor == 1:
            result = dividend
        elif dividend == 0:
            result = 0
        elif divisor > dividend:
            result = 0
        elif divisor == dividend:
            result = 1
        elif divisor < dividend:
            while dividend - divisor >= 0:
                dividend -= divisor
                result += 1

        return result * negative


class MyTest(TestCase):
    def test_(self):
        solution = Solution();
        cases = [
            (10, 3, 3),
            (1, 1, 1),
            (14, -2, -7),
            (-10, -3, 3),
            (-2147483648,  -1, 2147483648),
        ];
        for case in cases:
            with self.subTest(case):
                self.assertEqual(case[2], solution.divide(case[0], case[1]))
