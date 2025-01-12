from unittest import TestCase

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            result = 0
            if n - 1 >= 0:
                result += self.climbStairs(n - 1)
            if n - 2 >= 0:
                result += self.climbStairs(n - 2)

            return result

class Test(TestCase):
    def test(self):
        solution = Solution()
        for n in [
            (1,1),
            (2,2),
            (3,3),
            (5,8),
            (10,89),
            (20,10946),
            (30,1346269),
            # (45,1836311903),
        ]:
            with self.subTest(n):
                self.assertEqual(
                    n[1],
                    solution.climbStairs(n[0])
                )
