class Solution:
    def isValid(self, s: str) -> bool:
        closing_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        tracker: List[str] = []

        for char in s:
            if char in closing_map:
                if tracker and tracker[-1] == closing_map[char]:
                    tracker.pop()
                else:
                    return False
            else:
                tracker.append(char)

        return len(tracker) == 0
