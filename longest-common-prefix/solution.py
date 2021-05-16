class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        index = 0

        while True:
            common_letter = ''

            for word in strs:
                if index >= len(word):
                    return longest_prefix

                if not common_letter:
                    common_letter = word[index]

                if word[index] != common_letter:
                    return longest_prefix

            longest_prefix += common_letter
            index += 1

        return longest_prefix
