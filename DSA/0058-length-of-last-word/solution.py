class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        new_s = s.split()
        return len(new_s[-1])
