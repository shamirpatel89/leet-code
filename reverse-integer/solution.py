class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x_string = str(abs(x))
        x_string_reversed = x_string[::-1]

        result = int(x_string_reversed)
        if is_negative:
            result *= -1

        if -2**31 <= result <= 2**31 - 1:
            return result

        return 0
