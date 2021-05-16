class Solution:

    mapping: Dict[str, int] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    subtraction_mapping: Dict[str, Tuple] = {
        'I': ('V', 'X'),
        'X': ('L', 'C'),
        'C': ('D', 'M'),
    }

    def romanToInt(self, s: str)gith -> int:
        result = 0
        index = 0
        length = len(s)

        while index < length:
            symbol = s[index]
            value = self.mapping[symbol]

            if symbol in self.subtraction_mapping:
                if index < length - 1 and s[index + 1] in self.subtraction_mapping[symbol]:
                    index += 1
                    value = self.mapping[s[index]] - value

            result += value
            index += 1

        return result
