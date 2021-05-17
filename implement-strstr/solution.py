from unittest import TestCase

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or needle == haystack:
            return 0

        haystack_length = len(haystack)
        needle_length = len(needle)
        indices: List[int] = []

        if not haystack or needle_length > haystack_length:
            return -1

        for index in range(0, haystack_length):
            end_index = index + needle_length - 1
            start = haystack[index]
            if end_index >= haystack_length:
                break

            end = haystack[end_index]
            if start == needle[0] and end == needle[-1]:
                indices.append(index)

        for start in indices:
            for i in range(0, needle_length):
                if needle[i] != haystack[start + i]:
                    break
            else:
                return start

        return -1

class Test(TestCase):

    def test(self):
        solution = Solution()
        test_cases = [
            ['hello', 'll', 2],
            ['aaaaa', 'bba', -1],
            ['aaaab', 'aab', 2],
            ['a', 'a', 0],
            ['', '', 0],
            ['abc', 'c', 2],
            ['a' * ((5 * 10**4) - 1) + 'b', 'a' * 40851 + 'b', 9148],
        ]
        for test_case in test_cases:
            with self.subTest(test_case):
                self.assertEqual(
                    test_case[2],
                    solution.strStr(test_case[0], test_case[1])
                )
