class Solution:
    mapping: Dict[str, str] = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        results = []

        for index, digit in enumerate(digits):
            chars = self.mapping[digit]
            if index == 0:
                results = chars
            else:
                results = [
                    f'{previous}{char}'
                    for char in chars
                    for previous in results
                ]

        return results
