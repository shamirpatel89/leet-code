class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0

        while a or b or carry:
            if a:
                carry += int(a[-1])
            if b:
                carry += int(b[-1])
            sum, carry = carry % 2, carry // 2
            result = str(sum) + result

            a = a[:-1]
            b = b[:-1]

        return result
