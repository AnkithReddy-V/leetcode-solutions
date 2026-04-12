class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for c in s:
            if (c in freq):
                freq[c] += 1
            else:
                freq[c] = 1
        for index, c in enumerate(s):
            if (freq[c] == 1):
                return index
        return -1
        
