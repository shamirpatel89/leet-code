class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        carry = 1

        while carry and index >= 0:
            digit = digits[index] + carry
            digits[index], carry = digit % 10, digit // 10

            index -= 1

        if carry:
            digits = [1] + digits

        return digits
