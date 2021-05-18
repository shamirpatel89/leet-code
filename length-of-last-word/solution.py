class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        while i >= 0:
            if s[i] != ' ':
                break
            i -= 1

        if i < 0:
            return 0

        while i >= 0:
            if s[i] != ' ':
                length += 1
                i -= 1
            else:
                break

        return length

print(Solution().lengthOfLastWord('m '))
