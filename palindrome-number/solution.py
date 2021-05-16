class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        length = len(x_string)

        for index, digit in enumerate(x_string):
            opposite_index = length - 1 - index
            if index >= opposite_index:
                break
            if digit != x_string[opposite_index]:
                return False

        return True
